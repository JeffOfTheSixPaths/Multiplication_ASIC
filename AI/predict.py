import numpy as np
import h5py 
import os
import sys
sys.path.add("../Multiplication_ASIC")
from multiply import multiply as m
from tensorflow.keras.datasets import mnist

# Load the dataset into training and testing data
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

f = h5py.File('mnist_weightsh.h5', 'r')


weights = [f['dense']['dense'],
           f['dense_1']['dense_1']]
weights_nueron_num = [0]*len(weights)

data = 1
hidden_layers = 2
def predict(data):

    last_layer_output = data.flatten()
    
    for layer in range(hidden_layers):
        last_layer_output = ( relu(dot_pb(weights[layer], last_layer_output)) )
    
    #now all of the hidden layers have been computed
    # and now we have to computer the output layer

    probs = softmax(last_layer_output)
    return np.argmax(probs)



def softmax(i):
    return np.exp(i) / sum(np.exp(i))

def relu(f):
    return f*(f>0)

def dot_pb(wb, input):
    #wb[0] is the weights matrix
    #wb[1] is just the bias value
    #print(type(wb))
    #print(wb['kernel:0'].shape)
    #print(len(input))
    sum = dot(wb['kernel:0'], input)
    return np.array(sum) + np.array(wb['bias:0'])

def dot(vector_a, vector_b):
    return sum(multiply(a,b) for a, b in zip(vector_a, vector_b))   

def multiply(a, b):
    return m(a,b)

correct = 0
nums = {
}

total = 1000 #60k
for i, image in enumerate(test_images[:1000]):
    prediction = predict(image)
    label = test_labels[i]
    if prediction == label:
        correct += 1 
    else:
        nums[str(prediction) + " " + str(label)] = nums.get(str(prediction) + " " + str(label), 0) + 1

print(correct/total)

print(nums)
