import numpy as np
import random

def generate_random_values(size):
    """Generates a list of random floats between -1.0 and 1.0 rounded to 1 decimal."""
    return [round(random.uniform(-1.00, 1.00), 1) for _ in range(size)]

def generate_t_values(a, s, w):
    """Calculates recursive time-series values based on input noise w."""
    t = np.zeros(len(w))
    for i in range(1, len(w)):
        # Recursive formula: t[i] = -a * t[i-1] + s * w[i]
        t[i] = -a * t[i-1] + s * w[i]
    return t

def generate_a_values(b, g):
    """Applies a logarithmic transformation to the combined data b and g."""
    a = np.zeros(len(b))
    for i in range(len(b)):
        val = b[i] * g[i] + 150
        # Ensure the value is positive before applying log to avoid NaNs
        a[i] = np.log(val) if val > 0 else 0
    return a