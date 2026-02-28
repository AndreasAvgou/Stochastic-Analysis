def calculate_step_differences(data):
    """Calculates the difference between consecutive time steps (dx_t)."""
    return [data[i] - data[i-1] for i in range(1, len(data))]