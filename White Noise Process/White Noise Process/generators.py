import numpy as np
import random

def generate_random_noise(size):
    """Generates a list of random floats between -1.0 and 1.0 rounded to 1 decimal."""
    return [round(random.uniform(-1.00, 1.00), 1) for _ in range(size)]

def compute_random_walk(initial_value, sigma, noise_signal):
    """
    Computes a random walk process.
    Formula: t[i] = t[i-1] + sigma * w[i]
    """
    size = len(noise_signal)
    t = np.zeros(size)
    t[0] = initial_value
    
    for i in range(1, size):
        t[i] = t[i-1] + sigma * noise_signal[i]
    return t