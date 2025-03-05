import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def relu(x):
    return np.maximum(0, x)

def mlp(inputs, weights, biases, activation_function):
    layer_output = inputs
    for i, (w, b) in enumerate(zip(weights, biases)):
        layer_output = activation_function(np.dot(w, layer_output) + b)
        print(f"\nHidden Layer {i+1} Output:\n{layer_output}\n") #Debug
    return layer_output

def start():
  
    user_input = input("Enter your inputs separated by space: ")
    inputs = np.array([float(x) for x in user_input.split()])
    input_size = inputs.shape[0]

    num_hidden_layers = int(input("Enter number of hidden layers: "))
    hidden_size = int(input("Enter number of neurons per hidden layer: "))

    activation_choice = input("Choose activation function (sigmoid / relu): ").strip().lower()
    while activation_choice not in ["sigmoid", "relu"]:
        activation_choice = input(f"{activation_choice} is no valid input.\nChoose activation function (sigmoid / relu): ").strip().lower()
    activation_function = sigmoid if activation_choice == "sigmoid" else relu

    weights = [np.random.uniform(-1, 1, size=(hidden_size, input_size if i == 0 else hidden_size)) for i in range(num_hidden_layers)]
    biases = [np.random.uniform(-1, 1, size=(hidden_size,)) for _ in range(num_hidden_layers)]

    w_out = np.random.uniform(-1, 1, size=(1, hidden_size))
    b_out = np.random.uniform(-1, 1, size=(1,))

    weights.append(w_out)
    biases.append(b_out)

    output = mlp(inputs, weights, biases, activation_function)
    print("Final Output Layer:", output)

start()
