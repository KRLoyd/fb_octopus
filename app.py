#!/usr/bin/python3
"""
fb flask app
"""
from flask import Flask, render_template, request, jsonify, redirect, url_for
import json
import requests

app = Flask(__name__)
app.url_map.strict_slashes = False
host = '0.0.0.0'
port = 5000


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    renders template for main index
    """
    if request.method == 'GET':
        return render_template('index.html')

if __name__ == '__main__':
    """
    MAIN APP
    """
    app.run(host=host, port=port)
