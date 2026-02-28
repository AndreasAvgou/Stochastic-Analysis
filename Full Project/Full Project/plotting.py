import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf

def plot_and_save(data, filename, xlabel, ylabel, color='blue', smoothed=False):
    """Plots the data and saves the figure as a PDF file."""
    plt.figure()
    label = 'Smoothed' if smoothed else 'Original'
    plt.plot(data, label=label, color=color)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.savefig(filename, format='pdf')
    plt.close() # Close figure to free up memory

def plot_autocorr(data, filename, lags=100):
    """Generates and saves an Autocorrelation Function (ACF) plot."""
    plt.figure()
    plot_acf(data, lags=lags)
    plt.savefig(filename, format='pdf')
    plt.close()