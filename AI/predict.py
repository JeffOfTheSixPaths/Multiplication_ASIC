import numpy as np

weights = [[]]
weights_nueron_num = [0]*len(weights)
for i,layer in enumerate(weights):
    weights_nueron_num[i] = len(layer)

last_layer_output = []



data = 1
hidden_layers = 2
def predict(data):
    last_layer_output = data
    for layer in range(hidden_layers):
        out_data = []

        for nueron in weights[layer]:
            out_data.append( relu(dot_pb(nueron, last_layer_output)) )
        
        last_layer_output = out_data
    #now all of the hidden layers have been computed
    # and now we have to computer the output layer

    probs = softmax(last_layer_output)
    return probs.index(max(probs))



def softmax(i):
    return np.exp(xs) / sum(np.exp(xs))

def relu():
    return f*(f>0)

def dot_pb(wb, i):
    #wb[0] is the weights matrix
    #wb[1] is just the bias value
    sum = wb[1]
    for weight in wb[0]:
        sum += multiply(weight, i)

def multiply(a, b):
    return a*b

