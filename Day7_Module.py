#part of Day7
import math


def help():
    print(dir(math))

def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def multi(a, b):
    return a * b
def div(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b
def adiv(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a // b

