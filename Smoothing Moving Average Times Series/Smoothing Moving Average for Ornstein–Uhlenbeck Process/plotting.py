import matplotlib.pyplot as plt

def plot_smoothed_comparison(original, smoothed, label_name, title):
    """Plots original data against its smoothed version for visual comparison."""
    plt.figure(figsize=(15, 8))
    plt.plot(original, label=f'Original {label_name}', alpha=0.5)
    plt.plot(smoothed, label=f'Smoothed {label_name}', linewidth=2)
    plt.title(title)
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()