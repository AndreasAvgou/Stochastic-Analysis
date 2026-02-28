import matplotlib.pyplot as plt

def plot_time_series(data_list, titles, labels=None):
    """Plots multiple time series in a single figure for comparison."""
    plt.figure(figsize=(12, 6))
    for i, data in enumerate(data_list):
        label = labels[i] if labels else f'Series {i+1}'
        plt.plot(data, label=label)
    
    plt.title(" / ".join(titles))
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.legend()
    plt.show()

def plot_differences(diff1, diff2, title):
    """Plots the differences of two series to visualize the noise component."""
    plt.figure(figsize=(12, 6))
    plt.plot(diff1, label='Diff 1', alpha=0.8)
    plt.plot(diff2, label='Diff 2', alpha=0.6)
    plt.title(title)
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.legend()
    plt.show()