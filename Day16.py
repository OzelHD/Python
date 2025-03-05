# 1️⃣ Modify the perceptron to support user-defined inputs and weights.
# 2️⃣ Plot the sigmoid function from -10 to 10.
# 3️⃣ Try different input values and see how they affect the perceptron’s output.


import matplotlib.pyplot as plt
import numpy as np


def sigmoid(x):
    return(1 / (1 + np.exp(-x)))

def perceptron(inputs, weights, bias):
    return sigmoid(np.dot(inputs, weights) + bias)

num_inputs = int(input("Enter number of inputs: "))
inputs = np.array([float(input(f"Input {i+1}: ")) for i in range(num_inputs)])
weights = np.array([float(input(f"Weight {i+1}: ")) for i in range(num_inputs)])
bias = float(input("Enter bias value: "))


x = np.linspace(-10, 10, 100)
y = sigmoid(x)

plt.plot(x, y, color="blue", label="Sigmoid Function")
plt.axhline(0.5, linestyle="--", color="gray")
plt.xlabel("Input (x)")
plt.ylabel("Sigmoid Output")
plt.title("Sigmoid Activation Function")
plt.legend()
plt.grid()
plt.show()
