#!/usr/bin/python3

from flask import Flask,render_template,request,Response
from run_prediction import classify
import requests
import ast
import json
from eth_block import sendCrime
app = Flask(__name__)

@app.route('/post',methods=['POST'])
def post():
  print(request.form)
  print(type(request.form))
  form = ast.literal_eval(list(dict(request.form).keys())[0])
  try:
    classified,confidence = classify(form['Description'])[0]
  except Exception as e:
    print(e)
    classified,confidence = '',0
  data = {}
  data['body'] = form
  data['body']['Class'] = classified
  data['body']['Confidence'] = float(confidence)
  print(data['body']['Class'],data['body']['Confidence'])
  print(form)
  sendCrime(float(form['Latitude']),float(form['Longitude']),form['Class'])
  requests.post('https://gony0gqug0.execute-api.us-east-1.amazonaws.com/beta/post',json=data)
  resp = Response('')
  resp.headers['Access-Control-Allow-Origin'] = '*'
  return resp
