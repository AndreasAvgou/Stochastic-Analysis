import numpy as np
import random

def generate_wiener_noise(size):
    """Generates two independent noise signals for the Wiener Process simulation."""
    w1 = [round(random.uniform(-1.0, 1.0), 1) for _ in range(size)]
    w2 = [round(random.uniform(-1.0, 1.0), 1) for _ in range(size)]
    return np.array(w1), np.array(w2)

def simulate_wiener_process(size, sigma, noise):
    """
    Simulates the Wiener Process (Brownian Motion).
    Formula: t[i] = t[i-1] + sigma * sqrt(dt) * noise[i]
    where dt = 1 / size.
    """
    t = np.zeros(size)
    dt_sqrt = np.sqrt(1 / size)
    
    for i in range(1, size):
        t[i] = t[i-1] + sigma * dt_sqrt * noise[i]
    return t