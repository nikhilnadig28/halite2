import numpy as np
import logging
import random
from v1.Common import *


class NeuralNetwork(object):

    def __init__(self, nn_layer, weights):
        # parameters
        self.layer = nn_layer
        self.input_size = nn_layer[0]
        self.hidden_size = nn_layer[1]
        self.output_size = nn_layer[2]

        # weights
        self.weights = weights
        self.W1 = self.weights[:nn_layer[0]*nn_layer[1]].reshape([nn_layer[0], nn_layer[1]])
        self.W2 = self.weights[nn_layer[0]*nn_layer[1]:].reshape([nn_layer[1], nn_layer[2]])

    def forward(self, X):
        # forward propagation through our network
        z = np.dot(X, self.W1)  # dot product of X (input) and first set of 3x2 weights
        self.z2 = self.sigmoid(z)  # activation function

        z3 = np.dot(self.z2, self.W2)  # dot product of hidden layer (z2) and second set of 3x1 weights
        o = sigmoid(z3)  # final activation function
        return o

    def sigmoid(self, s):
        # activation function
        capping_indices = s > 100
        s[capping_indices] = 100
        capping_indices = s < -100
        s[capping_indices] = -100
        return 1/(1+np.exp(-s))

    def sigmoidPrime(self, s):
        #derivative of sigmoid
        return s * (1 - s)

    def backward(self, _X, _y, o):
        # backward propagate through the network
        o_error = _y - o  # error in output
        o_delta = o_error*self.sigmoidPrime(o)  # applying derivative of sigmoid to error

        z2_error = o_delta.dot(self.W2.T)  # z2 error: how much our hidden layer weights contributed to output error
        z2_delta = z2_error*self.sigmoidPrime(self.z2)  # applying derivative of sigmoid to z2 error

        self.W1 += _X.T.dot(z2_delta)  # adjusting first set (input --> hidden) weights
        self.W2 += self.z2.T.dot(o_delta)  # adjusting second set (hidden --> output) weights

    def train(self, X, y):
        o = self.forward(X)
        self.backward(X, y, o)

    def cross(self, nn2, split_index=None):
        if not split_index:
            split_index = random.randint(0, len(self.weights)-1)
        first_part = np.split(self.weights, [split_index + 1, len(self.weights)])
        last_part = np.split(nn2.weights, [split_index + 1, len(nn2.weights)])
        new_weights = np.concatenate([first_part[0], last_part[1]])
        new_nn = NeuralNetwork(self.layer, new_weights)
        return new_nn


# For Testing
if __name__ == '__main__':
    print("done")
    layer = np.array([2, 3, 2])
    NN = NeuralNetwork(layer)

    print(NN.weights)
    print(NN.W1)
    print(NN.W2)
    print(NN.weights[:layer[0] * layer[1]].reshape([2, 3]))
    print(NN.weights[layer[1] * layer[2]:].reshape([3, 2]))
