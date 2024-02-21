from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route('/myroute', methods=['GET'])
def hello_world():
    json_text = jsonify(some_data)

    # And then you can return it to the front end in the response body like this
    return json_text

@app.route('/todos', methods=['GET'])
def handle_todos():
    response_body = jsonify(todos)
    return response_body

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if position >= len(todos):
        response_body = {"message": "Tarea fuera de rango"}
        return response_body
    del todos[position]
    print("This is the position to delete:", position)
    return jsonify(todos)


# Suppose you have your data in the variable named some_data
some_data = { "name": "Bobby", "lastname": "Rixer" }
todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

# These two lines should always be at the end of your app.py file
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
