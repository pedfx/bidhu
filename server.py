
import os
import urllib
from flask import Flask, request
from werkzeug.utils import secure_filename
from html_page import HtmlReturn
from PIL import Image
import glob
import zipfile
import shutil
from test import Classificar



UPLOAD_FOLDER = str(os.getcwd())
ALLOWED_EXTENSIONS = set(['jpeg','zip'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
	return '.' in filename and \
		   filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS



@app.route('/', methods=['GET', 'POST'])
def upload_file():
	if request.method == 'GET':
		folder = UPLOAD_FOLDER + '/static/galaxies/'
		for erase in os.listdir(folder):
			file_path = os.path.join(folder, erase)
			if os.path.isfile(file_path):
				os.unlink(file_path)
	if request.method == 'POST':
		ra = (request.form['ra'])
		dec = (request.form['dec'])
		x = 0
		content1 = ''
		web = ''
		if ra!= "" and dec!= "" :

			x =1
			ra = float(ra)
			dec = float(dec)
			web = 'http://skyserver.sdss.org/dr12/SkyserverWS/ImgCutout/getjpeg?'\
					'TaskName=Skyserver.Chart.Image&ra='\
					+ str(ra) + '&dec=' + str(dec) + \
					'&width=512&height=512&scale=0.2'
			name = "RA{"+str(ra)+"}DEC{"+str(dec)+"}.jpeg"
			path = (os.path.join(app.config['UPLOAD_FOLDER'], name))
			urllib.urlretrieve(web, path)
			size = 80, 80
			im = Image.open(path)
			im.thumbnail(size, Image.ANTIALIAS)
			im.save(path, "JPEG")
			shutil.move(path, UPLOAD_FOLDER + '/static/galaxies/' +
						path.replace(str(os.getcwd()), "").replace("/", ""))


			web = "<a href= 'http://skyserver.sdss.org/dr12/en/tools/chart/image.aspx?ra=" \
				  + str(ra) + "&dec=" + str(dec) + \
				  "&width=512&height=512&scale=0.2'> " \
				  "Open on SDSS website.</a><br>"


			content1 = path

			class1 = Classificar()
			content2 = class1.rodar(x)
			class2 = HtmlReturn()
			html = class2.htmlstring(content1, content2, x, web )

			return html


		if 'file' not in request.files:
			return app.send_static_file('index.html')

		file = request.files['file']

		if file.filename == '':
			return app.send_static_file('index.html')


		if file and allowed_file(file.filename):

			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

			extension = filename.split('.')
			print extension

			if 'jpeg' in extension:
				x =1
				filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
				img = Image.open(filepath)
				size = 80, 80

				img.thumbnail(size, Image.ANTIALIAS)
				img.save((os.path.join(app.config['UPLOAD_FOLDER'] + '/static/galaxies/', filename)))
				shutil.move(filepath, UPLOAD_FOLDER + '/static/galaxies/' +
							filepath.replace(str(os.getcwd()), "").replace("/", ""))
				content1 = filepath + "<br>"


			if 'zip' in extension:
				zip = zipfile.ZipFile(filename, 'r')
				zip.extractall()
				x = 0
				content1 = ''
				for index in glob.glob(os.path.join(app.config['UPLOAD_FOLDER'], '*.jpeg')):
					x+=1
					content1 += index + "<br>"
					shutil.move(index, UPLOAD_FOLDER+'/static/galaxies/'+
								index.replace(str(os.getcwd()), "").replace("/", ""))

		if x!= 0:
				class1 = Classificar()
				content2 = class1.rodar(x)
				class2 = HtmlReturn()
				html = class2.htmlstring(content1, content2, x, web)
		else:
				html = app.send_static_file('error.html')

		return html



	return app.send_static_file('index.html')



port = os.getenv('PORT', '5000')
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(port))
