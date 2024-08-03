import os
import uuid

from flask import Flask
from flask import request, make_response, render_template, redirect, url_for, Response, send_from_directory,jsonify
import pandas as pd


app = Flask(__name__, template_folder='templates', static_folder="static", static_url_path="/")

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    

