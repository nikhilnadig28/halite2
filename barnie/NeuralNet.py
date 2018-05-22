import numpy as np
import logging
from Common import *

# Input data for test
X = np.array(([2, 9], [1, 5], [3, 6]), dtype=float)
y = np.array(([88], [89], [78]), dtype=float)

# scale units
X = X/np.amax(X, axis=0)  # maximum of X array
y = y/100  # max test score is 100


class NeuralNetwork(object):

    def __init__(self, nn_layer):
        # parameters
        input_size = nn_layer[0]
        output_size = nn_layer[1]
        hidden_size = nn_layer[2]

        logging.info(input_size)
        logging.info(output_size)
        logging.info(hidden_size)


        # weights
        self.W1 = np.random.randn(input_size, hidden_size)  # (17x10) weight matrix from input to hidden layer
        self.W2 = np.random.randn(hidden_size, output_size)  # (10x3) weight matrix from hidden to output layer

    def forward(self, _X):
        # forward propagation through our network
        logging.info(_X.shape)
        z = np.dot(_X, self.W1)  # dot product of X (input) and first set of 3x2 weights
        logging.info(z.shape)
        self.z2 = self.sigmoid(z)  # activation function
        logging.info(self.z2.shape)

        z3 = np.dot(self.z2, self.W2)  # dot product of hidden layer (z2) and second set of 3x1 weights
        logging.info(z3.shape)
        o = sigmoid(z3)  # final activation function
        return o

    def sigmoid(self, s):
        # activation function
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

    def train(self, _X, _y):
        o = self.forward(_X)
        self.backward(_X, _y, o)

    def crossover(self, weight_one, weight_two, split_index):
        first_part = np.split(weight_one, [split_index + 1, len(weight_one)])
        last_part = np.split(weight_two, [split_index + 1, len(weight_two)])
        return np.concatenate([first_part[0], last_part[1]])

    def set_weights(self, weights):
        pass

    def normalize_output(self, out):
        pass



#For Testing
if __name__ == 'main':
    layer = np.array([2,3,2])
    NN = NeuralNetwork(layer)
    for i in range(1000): # trains the NN 1,000 times
        pred_output = NN.forward(X)
        loss = np.mean(np.square(y - NN.forward(X)))
        if (i%100) == 0:
            print("Input: \n" + str(X))
            print("Actual Output: \n" + str(y))
            print("Predicted Output: \n" + str(pred_output))
            print("Loss: \n" + str(loss)) # mean sum squared loss
            print("\n")
        NN.train(X, y)