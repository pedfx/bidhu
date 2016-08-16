import matplotlib
import matplotlib.pyplot as plt
import matplotlib.cm as cm

from urllib import urlretrieve
import cPickle as pickle
import os
import gzip

import numpy as np
import theano

import lasagne
from lasagne import layers
from lasagne.updates import nesterov_momentum

from nolearn.lasagne import NeuralNet
from nolearn.lasagne import visualize

from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

from astropy.utils.data import download_file
from astropy.io import fits

from PIL import Image

np.set_printoptions(threshold=np.nan)


def load_dataset():
    X1 = np.zeros((1600, 19200), dtype=np.int)  # Allocate a 1600 X 19200 Matrix, each line corresponds to an image

    inp = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
           1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
           1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
           1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
           1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
           1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
           1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
           1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
           1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
           1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # Classification of the images

    aux = [i for i in range(1600)]

    count = 0
    count2 = 0

    np.random.shuffle(aux)

    inp2 = [i for i in range(1600)]
    cont = 0;

    for i in range(1, 1600):
        X1[aux[i - 1]] = np.asarray(
            Image.open("/Users/Pedro/PycharmProjects/bidhu/docs/galaxies/galaxy" + str(aux[i - 1] + 1) + ".jpg")).reshape(
            -1)[0:262144]  # Read input
        inp2[(i - 1)] = inp[(i - 1) % 200]  # Assign outputs
        cont = cont + 1

    X_train = np.zeros((1120, 19200), dtype=np.int)  # Assigns the training set
    y_train = np.zeros(1120, dtype=np.int)

    X_val = np.zeros((320, 19200), dtype=np.int)  # Assigns the validation set
    y_val = np.zeros(320, dtype=np.int)

    X_test = np.zeros((160, 19200), dtype=np.int)  # Assigns the testing set
    y_test = np.zeros(160, dtype=np.int)

    for i in range(0, 1120):  # Creates the training set
        X_train[i] = X1[i]
        y_train[i] = inp2[i]

    for i in range(1120, 1440):  # Creates the validation set
        X_val[i - 1120] = X1[i]
        y_val[i - 1120] = inp2[i]

    for i in range(1440, 1600):  # Creates the testing set
        X_test[i - 1440] = X1[i]
        y_test[i - 1440] = inp2[i];

    # This reshape is done to simplify the CNN execution
    X_train = X_train.reshape((-1, 3, 80, 80))
    X_val = X_val.reshape((-1, 3, 80, 80))
    X_test = X_test.reshape((-1, 3, 80, 80))

    y_train = y_train.astype(np.uint8)
    y_val = y_val.astype(np.uint8)
    y_test = y_test.astype(np.uint8)

    return X_train, y_train, X_val, y_val, X_test, y_test


X_train, y_train, X_val, y_val, X_test, y_test = load_dataset()

# Create Convolutional Neural Net, you may, should and must :) change this attributes to learn how a CNN works
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
            # ('dropout2', layers.DropoutLayer),
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
    update_learning_rate=0.003,
    update_momentum=0.9,
    max_epochs=1000,
    verbose=1,
)

nn = net1.fit(X_train, y_train)  # Train CNN

net1.save_params_to("/Users/Pedro/PycharmProjects/bidhu/docs/train.txt")  # Save CNN parameters
