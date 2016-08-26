import os
import glob
from flask import Flask


app = Flask(__name__)
UPLOAD_FOLDER = str(os.getcwd())
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

class Clean():

	def clean(self):

		folder = os.path.join(app.config['UPLOAD_FOLDER'], 'static', 'images', 'galaxies')

		for erase in os.listdir(folder):
			file_path = os.path.join(folder, erase)
			if os.path.isfile(file_path):
				os.unlink(file_path)
		folder = app.config['UPLOAD_FOLDER']

		for filetobeerased in glob.glob(os.path.join(UPLOAD_FOLDER, '*.jpeg')):
			file_path = os.path.join(folder, filetobeerased)
			if os.path.isfile(file_path):
					os.unlink(file_path)

		for filetobeerased in glob.glob(os.path.join(UPLOAD_FOLDER, '*.zip')):
			file_path = os.path.join(folder, filetobeerased)
			if os.path.isfile(file_path):
				os.unlink(file_path)