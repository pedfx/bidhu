import numpy as np
import lasagne
from lasagne import layers
from lasagne.updates import nesterov_momentum
from nolearn.lasagne import NeuralNet
from PIL import Image




class Classificar():
	#numerodeimagens = raw_input("Digite a quantidade de imagens a serem testadas:\n")
	#numerodeimagens = int(numerodeimagens)
	numerodeimagens = 5
	sourcepath = "/Users/Pedro/PycharmProjects/BIDHU/docs/safe test/"
	def rodar(self):

			np.set_printoptions(threshold=np.nan)
			sourcepath = Classificar.sourcepath
			numerodeimagens = Classificar.numerodeimagens

			X_test = np.zeros((numerodeimagens, 19200),
							  dtype=np.int)  # Allocates space for each new image you want to classify, each line is an image

			for i in range(1, numerodeimagens):  # read the images
				X_test[i - 1] = np.asarray(Image.open(sourcepath+"galaxy" + str(i) + ".jpg")).reshape(
					-1)[0:19200]

			# Reshape the images to help the CNN execution
			X_test = X_test.reshape((-1, 3, 80, 80))

			# Define the CNN, must be the same CNN that is saved into your model that you generated running CNN.py
			net1 = NeuralNet(
				layers=[('input', layers.InputLayer),
						('conv2d1', layers.Conv2DLayer),
						('maxpool1', layers.MaxPool2DLayer),
						('conv2d2', layers.Conv2DLayer),
						('maxpool2', layers.MaxPool2DLayer),
						('conv2d3', layers.Conv2DLayer),
						('maxpool3', layers.MaxPool2DLayer),
						# ('conv2d4', layers.Conv2DLayer),
						# ('maxpool4', layers.MaxPool2DLayer),
						('dropout1', layers.DropoutLayer),
						# s('dropout2', layers.DropoutLayer),
						('dense', layers.DenseLayer),
						# ('dense2', layers.DenseLayer),
						('output', layers.DenseLayer),
						],

				input_shape=(None, 3, 80, 80),

				conv2d1_num_filters=16,
				conv2d1_filter_size=(3, 3),
				conv2d1_nonlinearity=lasagne.nonlinearities.rectify,
				conv2d1_W=lasagne.init.GlorotUniform(),

				maxpool1_pool_size=(2, 2),

				conv2d2_num_filters=16,
				conv2d2_filter_size=(3, 3),
				conv2d2_nonlinearity=lasagne.nonlinearities.rectify,

				maxpool2_pool_size=(2, 2),

				conv2d3_num_filters=16,
				conv2d3_filter_size=(3, 3),
				conv2d3_nonlinearity=lasagne.nonlinearities.rectify,

				maxpool3_pool_size=(2, 2),

				# conv2d4_num_filters = 16,
				# conv2d4_filter_size = (2,2),
				# conv2d4_nonlinearity = lasagne.nonlinearities.rectify,

				# maxpool4_pool_size = (2,2),

				dropout1_p=0.5,

				# dropout2_p = 0.5,

				dense_num_units=16,
				dense_nonlinearity=lasagne.nonlinearities.rectify,

				# dense2_num_units = 16,
				# dense2_nonlinearity = lasagne.nonlinearities.rectify,

				output_nonlinearity=lasagne.nonlinearities.softmax,
				output_num_units=2,

				update=nesterov_momentum,
				update_learning_rate=0.001,
				update_momentum=0.9,
				max_epochs=1000,
				verbose=1,
			)

			net1.load_params_from("/Users/Pedro/PycharmProjects/BIDHU/docs/train.txt")  # Read model

			preds = net1.predict(X_test)  # make predictions


			strpreds = str(preds)
			strpreds = strpreds.replace(" ", "\n")

			strpreds = strpreds.replace("1", "yes")
			strpreds = strpreds.replace("0", "no")
			xstrpreds = (strpreds.splitlines())
			for i in range(len(xstrpreds)):
				xstrpreds[i] = str(i + 1) + "-" + xstrpreds[i]
			strpreds = str(xstrpreds)
			strpreds = strpreds.replace(" ", "\n")
			strpreds = strpreds.replace("[", "")
			strpreds = strpreds.replace("]", "")
			strpreds = strpreds.replace("'", "")
			strpreds = strpreds.replace(",", "")
			strpreds = strpreds.replace("-", " - ")

			return strpreds