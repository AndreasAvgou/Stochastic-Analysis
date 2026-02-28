def calculate_differences(data):
    """Calculates the increments (diffs) of the Wiener process."""
    return [data[i] - data[i-1] for i in range(1, len(data))]