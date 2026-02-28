import numpy as np

def apply_moving_average(data, window_size):
    """Applies a moving average smoothing filter to the input series."""
    return np.convolve(data, np.ones(window_size) / window_size, mode='valid')

def calculate_increments(data):
    """Calculates the differences between successive time steps."""
    return [data[i] - data[i-1] for i in range(1, len(data))]