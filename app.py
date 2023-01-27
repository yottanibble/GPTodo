from flask import Flask, jsonify, request

app = Flask(__name__)

todos = []

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify({'todos': todos})

@app.route('/todos', methods=['POST'])
def add_todo():
    todo = request.get_json()
    todos.append(todo)
    return jsonify({'todos': todos})

@app.route('/todos/<int:index>', methods=['PUT'])
def update_todo(index):
    todo = request.get_json()
    todos[index] = todo
    return jsonify({'todos': todos})

@app.route('/todos/<int:index>', methods=['DELETE'])
def delete_todo(index):
    todos.pop(index)
    return jsonify({'todos': todos})

if __name__ == '__main__':
    app.run(debug=True)