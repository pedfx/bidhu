from PIL import Image

for i in range(16):
    img = Image.open("/Users/Pedro/PycharmProjects/BIDHU/docs/galaxies/galaxy" + str(i + 1) + ".jpg").transpose(Image.FLIP_LEFT_RIGHT)
    img.save("/Users/Pedro/PycharmProjects/BIDHU/docs/galaxies/galaxy" + str(801 + i) + ".jpg")





# TO GALAXIES NOT MERGING


# img = Image.open("galaxiesnot/galaxy" + str(i + 1) + ".jpg").transpose(Image.FLIP_LEFT_RIGHT)
# img.save("galaxiesnot/galaxy" + str(41 + i) + ".jpg")

# for i in range(800):
#	img = Image.open("galaxies/galaxy" + str(i + 1) + ".jpg").transpose(Image.FLIP_TOP_BOTTOM)
#	img.save("galaxies/galaxy" + str(801 + i) + ".jpg")

#	img = Image.open("galaxiesnot/galaxy" + str(i + 1) + ".jpg").transpose(Image.FLIP_TOP_BOTTOM)
#	img.save("galaxiesnot/galaxy" + str(801 + i) + ".jpg")
