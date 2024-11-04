from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///user.db'

db = SQLAlchemy(app)
class database(db):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
@app.route('/')
def index():
    return "Hello"

if __name__ == '__main__':
    app.run(debug=True)