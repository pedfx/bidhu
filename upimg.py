import os
from flask import Flask, request
from html_page import HtmlReturn
from PIL import Image
import glob
import zipfile
from test import Classificar


app = Flask(__name__)
UPLOAD_FOLDER = str(os.getcwd())
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


class ImgUper:
	def upimger(self, filename):

		x = 0
		content1 = ''
		web = ''
		extension = filename.split('.')

		if 'jpeg' in extension:
			x = 1
			filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
			img = Image.open(filepath)
			size = 80, 80

			img.thumbnail(size, Image.ANTIALIAS)

			img.save(filepath)

			content1 = filepath

		if 'zip' in extension:
			zip = zipfile.ZipFile(filename, 'r')
			zip.extractall()
			x = 0
			content1 = ''
			for index in glob.glob(os.path.join(app.config['UPLOAD_FOLDER'], '*.jpeg')):
				x += 1
				content1 += index + '\n'

		if x != 0:
			class1 = Classificar()
			content2 = class1.rodar(x)
			class2 = HtmlReturn()
			html = class2.htmlstring(content1, content2, x, web)
		else:
			html = app.send_static_file('error.html')

		return html