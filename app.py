from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
else:
    app.debug = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# landing page route...
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/friends')
def friends():
    return render_template('friends.html')

if __name__ == '__main__':
    app.run()