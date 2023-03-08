from flask import Flask, request, jsonify
import requests
import json
import openai
import sys
import os

app = Flask(__name__)

from dotenv import load_dotenv
load_dotenv()

# fsa317@gmail.com
openai.api_key = os.environ.get('OPENAI_API_KEY') 

@app.route('/pyapi/pytest')
def test():
    rdata = {}
    rdata['test'] = "test"
    resp = jsonify(rdata)
    resp.status_code = 200
    return resp