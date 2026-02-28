import numpy as np
import random

def generate_ou_noise(size):
    """Generates random noise signals and coefficients rounded to 1 decimal."""
    w1 = [round(random.uniform(-1.00, 1.00), 1) for _ in range(size)]
    w2 = [round(random.uniform(-1.00, 1.00), 1) for _ in range(size)]
    a = [round(random.uniform(-1.00, 1.00), 1) for _ in range(size)]
    return np.array(w1), np.array(w2), np.array(a)

def simulate_ou_process(size, sigma, noise_w, coeffs_a):
    """
    Simulates the Ornstein-Uhlenbeck process.
    Formula: t[i] = -a[i] * t[i-1] + sigma * w[i]
    """
    t = np.zeros(size)
    t[0] = 1 # Initial state
    for i in range(1, size):
        t[i] = -coeffs_a[i] * t[i-1] + sigma * noise_w[i]
    return t