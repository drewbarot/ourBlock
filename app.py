from flask import Flask,render_template
from run_prediction import classify
import requests
app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/post',methods=['POST'])
def post():
  try:
    classified,confidence = classify(request.form['Description'])
  except:
    classified,confidence = '',0
  data['Class'] = classified
  data['Confidence'] = confidence
  requests.post('https://gony0gqug0.execute-api.us-east-1.amazonaws.com/beta/post',data=data)