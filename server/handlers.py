from flask import *
import numpy as np

# https://www.geeksforgeeks.org/python-import-module-outside-directory/
import importlib.util  
helpers_file = importlib.util.spec_from_file_location("helpers", "G:/_active/python_api/ml/helpers.py")   
helpers = importlib.util.module_from_spec(helpers_file)       
helpers_file.loader.exec_module(helpers)

def initHandlers():
    app = Flask(__name__)

    @app.route("/api/hello", methods=['GET'])
    def hello_world():
        return "<p>Hello, World!</p>"

    # ML

    # 1,1;0,0;1,0;0,1
    @app.route("/api/logic/disjunction", methods=['POST'])
    def disjunction():
        data = request.args.get('test', '')
        first_split = data.split(";")
        input = []

        for x in first_split:
            if len(x) > 0:
                temp = x.split(",")

                current = []
                current.append(int(temp[0]))
                current.append(int(temp[1]))
                input.append(current)

        first_split = ""

        MODEL = helpers.loadModel('disjunction.npy')
        DATA = np.array(input)
        response = helpers.predict_ann(DATA.T, MODEL)
        return [input, response.tolist()]

    @app.route("/api/logic/negation", methods=['POST'])
    def negation():
        data = request.args.get('test', '')
        first_split = data.split(";")
        input = []

        for x in first_split:
            if len(x) > 0:
                temp = x.split(",")

                current = []
                current.append(int(temp[0]))
                current.append(int(temp[1]))

                if ((current[0] == 1 and current[1] == 0) or (current[0] == 0 and current[1] == 1)):
                    continue

                input.append(current)

        first_split = ""

        MODEL = helpers.loadModel('negation.npy')
        DATA = np.array(input)
        response = helpers.predict_ann(DATA.T, MODEL)
        return [input, response.tolist()]

    @app.route("/api/logic/conjunction", methods=['POST'])
    def conjunction():
        data = request.args.get('test', '')
        first_split = data.split(";")
        input = []

        for x in first_split:
            if len(x) > 0:
                temp = x.split(",")

                current = []
                current.append(int(temp[0]))
                current.append(int(temp[1]))
                input.append(current)

        first_split = ""

        MODEL = helpers.loadModel('conjunction.npy')
        DATA = np.array(input)
        response = helpers.predict_ann(DATA.T, MODEL)
        return [input, response.tolist()]

    @app.route("/api/logic/implication", methods=['POST'])
    def implication():
        data = request.args.get('test', '')
        first_split = data.split(";")
        input = []

        for x in first_split:
            if len(x) > 0:
                temp = x.split(",")

                current = []
                current.append(int(temp[0]))
                current.append(int(temp[1]))
                input.append(current)

        first_split = ""

        MODEL = helpers.loadModel('implication.npy')
        DATA = np.array(input)
        response = helpers.predict_ann(DATA.T, MODEL)
        return [input, response.tolist()]
    # DB

    @app.route("/api/db/example", methods=['POST'])
    def postExample():
        return "<p>Hello, World!</p>"

    @app.route("/api/db/example", methods=['GET'])
    def scanExamples():
        return "<p>Test!</p>"

    @app.route("/api/db/example", methods=['PUT'])
    def updateExample():
        return "<p>Hello, World!</p>"

    @app.route("/api/db/example/<id>", methods=['GET'])
    def getExample(id):
        return "<p>Test!</p>"

    @app.route("/api/db/example/<id>", methods=['DELETE'])
    def deleteExample(id):
        return "<p>Test!</p>"

    app.run()