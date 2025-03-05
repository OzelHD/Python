# 1️⃣ Modify the perceptron to take three input values instead of two.
# 2️⃣ Change the activation function to a sigmoid function.
# 3️⃣ Test different input values and observe the results.

import numpy as np


def activation(x):
    return 1 if x >= 0 else 0

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def perceptron(inputs, weights, bias):
    linear_out = np.dot(inputs, weights) + bias
    return activation(linear_out), sigmoid(linear_out)

inputs = np.array([[12, 2, 4],
                   [31, 2, 9],
                   [0, 12, 2],
                   [0, 0, 20],
                   [9, 18, 7],
                   [11, 9, 2]])

weights = np.array([0.5, -0.5, 0.25])
bias = 0.2
for i in inputs:
    output1, output2 = perceptron(i, weights, bias)
    print(f"Perceptron Output: {output1}, {output2}")