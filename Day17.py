# 1️⃣ Modify the code to take user-defined input size, weights, and biases.
# 2️⃣ Try different sets of weights and biases to see how they affect the output.
# 3️⃣ (Optional) Extend this to a second hidden layer!


import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def perceptron(inputs, weights, bias):
    return sigmoid(np.dot(inputs, weights) + bias)

def feed_forward(inputs, weights, bias):
    return sigmoid(np.dot(inputs, weights) + bias)

num_inputs = input("Enter number of inputs: (TEST for tester inputs)\n")

if num_inputs == "TEST":
    inputs = np.array([2.3, 9.2, 10.3, 30.2, 22.8, 21.6, 44.2, 39.8, 0.2, 0.1], dtype=float)
    weights = np.array([3.1, 3.2, 9.0, 1.2, 1.9, 4.6, 3.1, 8.2, 0.31, 0.2], dtype=float)
    bias1 = -30.02
else:
    num_inputs = int(num_inputs)
    inputs = np.array([float(input(f"Input {i+1}: ")) for i in range(num_inputs)])
    weights = np.array([float(input(f"Weight {i+1}: ")) for i in range(num_inputs)])
    bias1 = float(input("Enter bias value: "))

weights2 = np.random.uniform(0, 1, size=1) 
bias2 = 3.2

output1 = perceptron(inputs, weights, bias1)
output2 = feed_forward(output1, weights2, bias2)

print(f"Perceptron Output (Layer 1):   {output1:.4f}")
print(f"Feed-Forward Output (Layer 2): {output2.item():.4f}")