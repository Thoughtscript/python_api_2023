from init import get_app

"""
Test endpoints.
"""

app = get_app()

@app.route("/api/hello", methods=['GET'])
def hello_world():
    return "<p>Hello, World!</p>"