from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
DATABASE_URL = 'postgresql://postgres:psuserpassword@localhost/myDB'
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL

# initialize sql-alchemy
db = SQLAlchemy()
db.init_app(app)


@app.route('/hello',methods=['GET','POST'])
def hello():
    if request.method == 'POST':
        username = request.get_json()['name']
        return "hello %s"%username
    else:
        return "hello"


@app.route('/insert',methods=['POST'])
def insert_task():
    try:
        task_name = request.get_json()['name']
        sql = "INSERT INTO tasks (name) VALUES ("+task_name+")"
        db.engine.execute(text(sql).execution_options(autocommit=True))
        return 200
    except Exception as e:
        return jsonify(status=500, response=e)


@app.route('/get_count', methods=['GET'])
def get_count():
    try:
        sql = "SELECT COUNT(*) FROM tasks"
        res = db.engine.execute(sql).fetchall()
        return jsonify(
            status=200,
            response=res[0]
        )
    except Exception as e:
        return jsonify(status=500, response=e)
