# coding=utf-8
from PIL import Image
import os

print os.getcwd()

for i in range(200):
    img = Image.open("galaxies/galaxy" + str(i + 1) + ".jpg")

    img = img.rotate(90)
    img.save("galaxies/galaxy" + str(201 + i) + ".jpg")

    img = img.rotate(90)
    img.save("galaxies/galaxy" + str(401 + i) + ".jpg")

    img = img.rotate(90)
    img.save("galaxies/galaxy" + str(601 + i) + ".jpg")





# TO GALAXIES NOT MERGING



# for i in range(600):
#	img = Image.open("galaxiesnot/galaxy" + str(i + 1) + ".jpg")

#	img = img.rotate(90)
#	img.save("galaxiesnot/galaxy"+ str(101 + i) +".jpg")

#	img = img.rotate(90)
#	img.save("galaxiesnot/galaxy"+ str(201 + i) +".jpg")

#	img = img.rotate(90)
#	img.save("galaxiesnot/galaxy"+ str(301 + i) +".jpg")
