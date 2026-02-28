import numpy as np

def apply_moving_average(data, window_size):
    """Applies a simple moving average filter using convolution."""
    return np.convolve(data, np.ones(window_size) / window_size, mode='valid')

def calculate_increments(data):
    """Calculates the first-order differences (increments) of the series."""
    return [data[i] - data[i-1] for i in range(1, len(data))]