from flask import Flask, request
import urllib
from PIL import Image
import os
from test import Classificar
from html_page import HtmlReturn

app = Flask(__name__)
UPLOAD_FOLDER = str(os.getcwd())
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

class ImgGetter():
	def getimg(self):
		ra = (request.form['ra'])
		dec = (request.form['dec'])
		x = 0
		content1 = ''
		web = ''
		if ra != "" and dec != "":
			x = 1
			ra = float(ra)
			dec = float(dec)
			web = 'http://skyserver.sdss.org/dr12/SkyserverWS/ImgCutout/getjpeg?' \
				  'TaskName=Skyserver.Chart.Image&ra=' \
				  + str(ra) + '&dec=' + str(dec) + \
				  '&width=512&height=512&scale=0.2'
			name = "RA{" + str(ra) + "}DEC{" + str(dec) + "}.jpeg"
			path = (os.path.join(app.config['UPLOAD_FOLDER'], name))
			urllib.urlretrieve(web, path)
			size = 80, 80
			im = Image.open(path)
			im.thumbnail(size, Image.ANTIALIAS)
			im.save(path, "JPEG")

			web = "<a href= 'http://skyserver.sdss.org/dr12/en/tools/chart/image.aspx?ra=" \
				  + str(ra) + "&dec=" + str(dec) + \
				  "&width=512&height=512&scale=0.2'> " \
				  "Open on SDSS website.</a><br>"

#			for root, dirs, files in os.walk(os.getcwd()):
#				if imagetobefound in files:
#					print os.path.join(root, imagetobefound)

			content1 = path

			class1 = Classificar()
			content2 = class1.rodar(x)
			class2 = HtmlReturn()
			html = class2.htmlstring(content1, content2, x, web)

			return html