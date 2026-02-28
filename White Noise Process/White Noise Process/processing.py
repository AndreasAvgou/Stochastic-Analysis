def calculate_differences(data):
    """Computes the difference between successive values (the return of the walk)."""
    return [data[i] - data[i-1] for i in range(1, len(data))]