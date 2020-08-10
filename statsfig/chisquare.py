from scipy import stats
import numpy as np
import matplotlib.pyplot as plt


def chifig(size=8, dof=[1, 4, 6, 7], fig_w=8, fig_l=8, grid=True):
    """
    parameters
    ----------
    dof: default [1,4,6,7], Degree of freedoms to display
    fig_w: default: 8, Matplotlib `figsize` width
    fig_l: default: 8, Matplotlib `figsize` length
    grid: default True, Use 'True' or 'False'

    examples
    --------
    import statfig as sf

    sf.chifig()

    sf.chifig(dof=[1,4])

    """

    fig, ax = plt.subplots(1, 1, figsize=(fig_w, fig_l))
    x = np.linspace(0, 10, 100)
    linestyles = [':', '--', '-.', '-', ':', '--', '-.', '-']

    dof = dof
    for df, ls in zip(dof, linestyles):
        ax.plot(x, stats.chi2.pdf(x, df), linestyle=ls)

    ax.set_xlim(0, 10)
    ax.set_ylim(0, 0.4)

    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.set_title('Chi-Square Distribution')

    ax.legend(dof, loc='best', frameon=True)
    ax.grid(grid)
    plt.show()
