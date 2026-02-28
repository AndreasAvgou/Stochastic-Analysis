import matplotlib.pyplot as plt

def plot_wiener_series(data, label, title, color='blue'):
    """Plots a single Wiener process time series."""
    plt.figure(figsize=(15, 8))
    plt.plot(data, label=label, color=color)
    plt.title(title)
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()

def plot_difference_series(diff_data, label, title, color='orange'):
    """Plots the differences (increments) of the process."""
    plt.figure(figsize=(15, 8))
    plt.plot(diff_data, label=label, color=color)
    plt.title(title)
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()