from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt


def nd():
    fig, ax = plt.subplots()
    # for distribution curve
    x = np.arange(-4, 4, 0.001)
    ax.plot(x, norm.pdf(x))
    ax.set_title("Cumulative normal distribution")
    ax.set_xlabel('x')
    ax.set_ylabel('pdf(x)')
    ax.grid(True)
    # for fill_between
    px = np.arange(-4, 1, 0.01)
    ax.set_ylim(0, 0.5)
    ax.fill_between(px, norm.pdf(px), alpha=0.5, color='g')
    # for text
    ax.text(-1, 0.1, "cdf(x)", fontsize=20)
    plt.show()
