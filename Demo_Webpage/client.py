from flask import Flask,jsonify, url_for, Response, render_template, make_response, redirect
from flask_restful import reqparse, request
import requests,html,urllib.parse
import json, requests, os, sys

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
	with open('./static/img/file.txt') as f:
		jsonData = json.load(f)
	text_label = jsonData['text_label']
	text_label_en = jsonData['text_label_en']
	image_label = []
	image_label_en = []
	result = jsonData['result']
	for i, value in enumerate(jsonData['label']):
		image_label.append(jsonData['label'][value]['cn'])
		image_label_en.append(jsonData['label'][value]['en'])
	return render_template('index.html', text_label = text_label, text_label_en = text_label_en, image_label=image_label, image_label_en = image_label_en , result=result), 200
	
@app.route('/char', methods=['GET'])
def character():
	with open('./static/img/char/file.txt') as f:
			jsonData = json.load(f)
			
	label_list = []
	predict_list = []
	result_list = []
	correct = 0
	wrong = 0
	accuracy = 0
	for key in jsonData:
		label_list.append(jsonData[key]['label'])
		predict_list.append(jsonData[key]['predict'])
		result_list.append(jsonData[key]['result'])
		if jsonData[key]['result'] == True:
			correct += 1
		else:
			wrong += 1
	accuracy = '%.2f' % (correct/len(label_list))
	return render_template('character.html', length = len(label_list),label_list = label_list,  predict_list = predict_list, result_list = result_list, total=len(label_list),correct=correct, wrong=wrong, accuracy=accuracy), 200

def run():
	app.config['JSON_AS_ASCII'] = False
	app.run(debug=True , port=5000)

if __name__ == "__main__":
	app.config['JSON_AS_ASCII'] = False
	app.run(debug=True , port=5000)