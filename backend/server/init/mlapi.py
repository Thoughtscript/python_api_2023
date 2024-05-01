from init import get_app
from flask import request
import numpy as np

# https://www.geeksforgeeks.org/python-import-module-outside-directory/
import importlib.util  
helpers_file = importlib.util.spec_from_file_location("helpers", "/app/ml/helpers.py")   
helpers = importlib.util.module_from_spec(helpers_file)       
helpers_file.loader.exec_module(helpers)

"""
ML endpoints.
"""

app = get_app()

# Load these once
DISJUNCTION_MODEL = helpers.loadModel('disjunction.npy')
NEGATION_MODEL = helpers.loadModel('negation.npy')
CONJUNCTION_MODEL = helpers.loadModel('conjunction.npy')
IMPLICATION_MODEL = helpers.loadModel('implication.npy')

async def handleRequest(request, reject_unsame = False):
    data = request.args.get('test', '')
    supplied_bool_vals = data.split("|")
    input = []
    for x in supplied_bool_vals:
        if len(x) > 0:
            temp = x.split(",")

            current = []
            current.append(int(temp[0]))
            current.append(int(temp[1]))

            if reject_unsame:
                if ((current[0] == 1 and current[1] == 0) or (current[0] == 0 and current[1] == 1)):
                    continue

            input.append(current)

    return input
    
@app.route("/api/logic/disjunction", methods=['POST'])
async def disjunction():
    input = await handleRequest(request)
    DATA = np.array(input)
    response = helpers.predict_ann(DATA.T, DISJUNCTION_MODEL)
    return [input, response.tolist()]

@app.route("/api/logic/negation", methods=['POST'])
async def negation():
    input = await handleRequest(request, True)
    DATA = np.array(input)
    response =  helpers.predict_ann(DATA.T, NEGATION_MODEL)
    return [input, response.tolist()]

@app.route("/api/logic/conjunction", methods=['POST'])
async def conjunction():
    input = await handleRequest(request)
    DATA = np.array(input)
    response = helpers.predict_ann(DATA.T, CONJUNCTION_MODEL)
    return [input, response.tolist()]

@app.route("/api/logic/implication", methods=['POST'])
async def implication():
    input = await handleRequest(request)
    DATA = np.array(input)
    response = helpers.predict_ann(DATA.T, IMPLICATION_MODEL)
    return [input, response.tolist()]