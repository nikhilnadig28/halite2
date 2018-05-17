import numpy as np

# Input data for test
X = np.array(([2, 9], [1, 5], [3, 6]), dtype=float)
y = np.array(([88], [89], [78]), dtype=float)

# scale units
X = X/np.amax(X, axis=0) # maximum of X array
y = y/100 # max test score is 100

class Neural_Network(object):
    def __init__(self, layer):
        #parameters
        self.inputSize = layer[0]
        self.outputSize = layer[1]
        self.hiddenSize = layer[3]

        #weights
        self.W1 = np.random.randn(self.inputSize, self.hiddenSize) # (3x2) weight matrix from input to hidden layer
        self.W2 = np.random.randn(self.hiddenSize, self.outputSize) # (3x1) weight matrix from hidden to output layer

    def forward(self, X):
        #forward propagation through our network
        self.z = np.dot(X, self.W1) # dot product of X (input) and first set of 3x2 weights
        self.z2 = self.sigmoid(self.z) # activation function
        self.z3 = np.dot(self.z2, self.W2) # dot product of hidden layer (z2) and second set of 3x1 weights
        o = self.sigmoid(self.z3) # final activation function
        return o

    def sigmoid(self, s):
        # activation function
        return 1/(1+np.exp(-s))

    def sigmoidPrime(self, s):
        #derivative of sigmoid
        return s * (1 - s)

    def backward(self, X, y, o):
        # backward propgate through the network
        self.o_error = y - o # error in output
        self.o_delta = self.o_error*self.sigmoidPrime(o) # applying derivative of sigmoid to error

        self.z2_error = self.o_delta.dot(self.W2.T) # z2 error: how much our hidden layer weights contributed to output error
        self.z2_delta = self.z2_error*self.sigmoidPrime(self.z2) # applying derivative of sigmoid to z2 error

        self.W1 += X.T.dot(self.z2_delta) # adjusting first set (input --> hidden) weights
        self.W2 += self.z2.T.dot(self.o_delta) # adjusting second set (hidden --> output) weights

    def train (self, X, y):
        o = self.forward(X)
        self.backward(X, y, o)

    def crossover(self, weight_one, weight_two, split_index):
        first_part = np.split(weight_one, [split_index + 1, len(weight_one)])
        last_part = np.split(weight_two, [split_index + 1, len(weight_two)])
        o = np.concatenate([first_part[0], last_part[1]])
        return o

    def set_weights(self, weights):
        pass

    def normalize_output(self, out):



#For Testing
if __name__ == 'main':
    NN = Neural_Network()
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