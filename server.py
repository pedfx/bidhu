#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from flask import Flask, request
from werkzeug.utils import secure_filename
from cleaner import Clean
from getimg import ImgGetter
from upimg import ImgUper

UPLOAD_FOLDER = str(os.getcwd())
ALLOWED_EXTENSIONS = set(['jpeg', 'zip'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
	return '.' in filename and \
		   filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
	if request.method == 'GET':
		call = Clean()
		call.clean()


	if request.method == 'POST':
		ra = (request.form['ra']);
		dec = (request.form['dec'])

		if ra != "" and dec != "":
			call = ImgGetter()
			return call.getimg()

		if 'file' not in request.files:
			return app.send_static_file('index.html')

		file = request.files['file']

		if file.filename == '':
			return app.send_static_file('index.html')

		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

			call = ImgUper()
			return call.upimger(filename)

	return app.send_static_file('index.html')


port = os.getenv('PORT', '5000')
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(port))
