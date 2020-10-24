import flask ## Import flask library
from flask import request ## will use this to receive the request
import pandas as pd
from datetime import datetime as dt

app = flask.Flask(__name__) ## make a flask app

@app.route('/', methods=['GET'])
def home():
    q = int(request.args['q'])
    try:
        return q
    except KeyError:
        return KeyError
