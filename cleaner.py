import os
import glob
import shutil

class Clean():
	def clean(self, UPLOAD_FOLDER):
		folder = UPLOAD_FOLDER + '/static/galaxies/'

		if glob.glob(os.path.join(UPLOAD_FOLDER, '__MACOSX')):
			shutil.rmtree(os.path.join(UPLOAD_FOLDER, '__MACOSX'))
		for erase in os.listdir(folder):
			file_path = os.path.join(folder, erase)
			if os.path.isfile(file_path):
				os.unlink(file_path)
		folder = UPLOAD_FOLDER
		for filetobeerased in glob.glob(os.path.join(UPLOAD_FOLDER, '*.jpeg')):
			file_path = os.path.join(folder, filetobeerased)
			if os.path.isfile(file_path):
					os.unlink(file_path)
		for filetobeerased in glob.glob(os.path.join(UPLOAD_FOLDER, '*.zip')):
			file_path = os.path.join(folder, filetobeerased)
			if os.path.isfile(file_path):
				os.unlink(file_path)