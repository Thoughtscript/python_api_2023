from init import get_app
from flask import request
from domain import scan_examples, get_example, delete_example, create_example, update_example

"""
DB endpoints.
"""

app = get_app()

@app.route("/api/db/example", methods=['POST'])
def postExample():
    name = request.form.get('name', '')
    result = create_example(name)

    return [str(result)]

@app.route("/api/db/examples", methods=['GET'])
def scanExamples():
    results = scan_examples()
    response = []

    for x in results:
        response.append(str(x))

    return response

@app.route("/api/db/example/<id>", methods=['PUT'])
def updateExample(id):
    name = request.form.get('name', '')
    result = update_example(id, name)

    return [str(result)]

@app.route("/api/db/example/<id>", methods=['GET'])
def getExample(id):
    result = get_example(id)

    return [str(result)]

@app.route("/api/db/example/<id>", methods=['DELETE'])
def deleteExample(id):
    result = delete_example(id)

    return [str(result)]
