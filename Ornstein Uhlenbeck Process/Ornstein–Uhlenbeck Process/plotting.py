import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf

def plot_process_and_diff(process_data, diff_data, title):
    """Plots both the primary process and its differences on the same chart."""
    plt.figure(figsize=(12, 6))
    plt.plot(process_data, label='OU Process')
    plt.plot(diff_data, label='Step Difference', alpha=0.7)
    plt.title(title)
    plt.legend()
    plt.show()

def plot_autocorrelation(data, lags=500):
    """Generates the ACF plot to analyze the memory of the process."""
    plot_acf(data, lags=lags)
    plt.show()