import numpy as np
import random

def generate_noise_signals(size):
    """Generates lists of random floats between -1.0 and 1.0 rounded to 1 decimal."""
    w1 = [round(random.uniform(-1.00, 1.00), 1) for _ in range(size)]
    w2 = [round(random.uniform(-1.00, 1.00), 1) for _ in range(size)]
    a = [round(random.uniform(-1.00, 1.00), 1) for _ in range(size)]
    return w1, w2, a

def simulate_ou_process(a_coeffs, sigma, noise_w):
    """
    Simulates the Ornstein-Uhlenbeck process.
    Equation: dx_t = -a * x_t * dt + sigma * W_dt
    """
    t_values = np.zeros(len(noise_w))
    t_values[0] = 1 # Initial condition
    
    for i in range(1, len(noise_w)):
        # Discrete approximation of the SDE
        t_values[i] = -a_coeffs[i] * t_values[i-1] + sigma * noise_w[i]
        
    return t_values