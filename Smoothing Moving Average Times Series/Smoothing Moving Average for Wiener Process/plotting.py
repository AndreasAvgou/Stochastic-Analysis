import matplotlib.pyplot as plt

def plot_smoothed_comparison(original, smoothed, label_name, title):
    """Visualizes the original noisy process against its smoothed moving average."""
    plt.figure(figsize=(15, 8))
    plt.plot(original, label=f'Original {label_name}', alpha=0.4, color='gray')
    plt.plot(smoothed, label=f'Smoothed {label_name}', linewidth=2)
    plt.title(title)
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()