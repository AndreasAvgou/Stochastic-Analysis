import numpy as np
import random

def generate_wiener_noise(size):
    """Generates two independent noise signals rounded to 1 decimal place."""
    w1 = [round(random.uniform(-1.0, 1.0), 1) for _ in range(size)]
    w2 = [round(random.uniform(-1.0, 1.0), 1) for _ in range(size)]
    return np.array(w1), np.array(w2)

def compute_wiener_process(size, sigma, noise):
    """
    Computes the Wiener Process (Brownian Motion) values.
    Formula: t[i] = t[i-1] + sigma * sqrt(dt) * noise[i]
    where dt is represented as 1/size.
    """
    t = np.zeros(size)
    dt_sqrt = np.sqrt(1 / size)
    
    for i in range(1, size):
        t[i] = t[i-1] + sigma * dt_sqrt * noise[i]
    return t