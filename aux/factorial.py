from PIL import Image



x = 6

for i in range(24):
	for i in range(5):

		img = Image.open("/Users/Pedro/PycharmProjects/BIDHU/docs/test/galaxy" + str(i + 1) + ".jpg")
			#.transpose(Image.FLIP_LEFT_RIGHT)
		img.save("/Users/Pedro/PycharmProjects/BIDHU/docs/test/galaxy" + str(x + i) + ".jpg")
		x = x + 1

