from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.s2sks.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/todo', methods=["POST"])
def add_todo():
    todo = request.form['todo_send']
    doc = {
        'todo': todo,
        'done': 0
    }
    db.todolist.insert_one(doc)
    return jsonify({'msg': 'POST 등록 완료'})


@app.route('/todo', methods=["GET"])
def get_todo():
    todos = list(db.todolist.find({}, {'_id': False}))
    return jsonify({'todo_list': todos})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
