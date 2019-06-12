import tensorflow as tf
import tflearn
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression
import numpy as np
import os
LR = 1e-4


class DnnModel:

    PATH = 'train_data.npy'   # path to data which consist of numpy array. C:\Users\HP\Documents\OMRD

    def __init__(self, img_w=40, img_h=40, lr=1e-4):
        self.width = img_w
        self.height = img_h
        self.data = np.load(self.PATH)
        self.lr = lr

    """
        divide numpy array into tran and test 
        @:return train(array) , test(array)
    """
    def create_train_test(self):
        train = self.data[:-50]
        test = self.data[-50:]
        return train, test

    """
        create convolution neural network model with help 
        of NVIDIA.
        @:return model
    """
    def model_creation(self):

        train, test = self.create_train_test()
        tf.reset_default_graph()

        MODEL_NAME = 'opticalmark-{}-{}.model'.format(LR, '2conv-basic')

        convnet = input_data(shape=[None, self.width, self.height, 1], name='input')

        convnet = conv_2d(convnet, 32, 5, activation='relu')
        convnet = max_pool_2d(convnet, 5)

        convnet = conv_2d(convnet, 64, 5, activation='relu')
        convnet = max_pool_2d(convnet, 5)

        convnet = conv_2d(convnet, 64, 5, activation='relu')
        convnet = max_pool_2d(convnet, 5)

        convnet = conv_2d(convnet, 32, 5, activation='relu')
        convnet = max_pool_2d(convnet, 5)

        convnet = fully_connected(convnet, 1024, activation='relu')
        convnet = dropout(convnet, 0.8)

        convnet = fully_connected(convnet, 2, activation='softmax')
        convnet = regression(convnet, optimizer='adam', learning_rate=self.lr, loss='categorical_crossentropy', name='targets')

        model = tflearn.DNN(convnet, tensorboard_dir='log')
        if os.path.exists('{}.meta'.format(MODEL_NAME)):
            model.load(MODEL_NAME)
            # print('model loaded!')

        # X = np.array([i[0] for i in train]).reshape(-1, self.width, self.height, 1)
        # Y = [i[1] for i in train]
        #
        # test_x = np.array([i[0] for i in test]).reshape(-1, self.width, self.height, 1)
        # test_y = [i[1] for i in test]
        #
        # model.fit({'input': X}, {'targets': Y}, n_epoch=9, validation_set=({'input': test_x}, {'targets': test_y}), snapshot_step=1000, show_metric=True)

        model.save(MODEL_NAME)

        return model

