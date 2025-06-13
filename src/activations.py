import math
import numpy as np

def tanh(x):
    return np.tanh(x)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def hard_sigmoid(x):
    return max(0, min(1, 0.2 * x + 0.5))

def relu(x):
    return max(0, x)

def leaky_relu(x, alpha=0.01):
    return x if x > 0 else alpha * x

def elu(x, alpha=1.0):
    return x if x >= 0 else alpha * (np.exp(x) - 1)

def softplus(x):
    return np.log(1 + np.exp(x))

def swish(x):
    return x / (1 + np.exp(-x))

def gelu(x):
    return 0.5 * x * (1 + np.tanh(np.sqrt(2 / np.pi) * (x + 0.044715 * x ** 3)))

def hard_swish(x):
    return x * max(0, min(1, (x + 3) / 6))