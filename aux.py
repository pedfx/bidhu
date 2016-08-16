

import zipfile
import os

filename = "galaxy.zip"
UPLOAD_FOLDER = os.getcwd()


print os.path.join(UPLOAD_FOLDER + '/static/galaxies/', filename)
