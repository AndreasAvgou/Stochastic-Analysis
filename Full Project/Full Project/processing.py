import numpy as np

def generate_smoothed_values(data, window_size):
    """Applies a moving average filter using a specific window size."""
    return np.convolve(data, np.ones(window_size) / window_size, mode='valid')

def calculate_differences(data):
    """Calculates the first-order difference between consecutive elements."""
    return [data[i] - data[i-1] for i in range(1, len(data))]