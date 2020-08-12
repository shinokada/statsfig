from scipy import stats
import numpy as np
import matplotlib.pyplot as plt


def chifig(dof=[1, 4, 6, 7], fig_w=8, fig_l=8, grid=True, font_size=20,
           title='Chi-Square Distribution', xlabel='Value', ylabel='Frequency',
           legend_size=12, title_size=20, label_size=16, tick_size=12):
    """

    parameters
    ----------

    dof: Degree of freedoms to display, the default value is [1,4,6,7]
    fig_w: Matplotlib `figsize` width, the default value is  8
    fig_l: Matplotlib `figsize` length, the default value is 8 
    grid: Use 'True' or 'False' to show the grid. The default value is 'True'. 
    title: The figure's title. The default value is 'Chi-Square Distribution'.
    xlabel: The x-axis label. The default value is 'Value'.
    ylabel: The y-axis label. The default value is 'Frequency'.
    legend_size: The legend font size. The default value is 12.
    title_size: Title font size. The default value is 20.
    label_size: Label font size. The default value is 16.
    tick_size: x and y axis tick font size. The default value is 12. 

    examples
    --------
    import statfig as sf

    sf.chifig()
    sf.chifig(title='Chi-Square Distribution for 1, 4, 6, 7')
    sf.chifig(dof=[1,4],title='Chi-Square Distribution for dof=1,4')

    """

    fig, ax = plt.subplots(1, 1, figsize=(fig_w, fig_l))
    x = np.linspace(0, 10, 100)
    linestyles = [':', '--', '-.', '-', ':', '--', '-.', '-']

    for df, ls in zip(dof, linestyles):
        ax.plot(x, stats.chi2.pdf(x, df), linestyle=ls)

    ax.set_xlim(0, 10)
    ax.set_ylim(0, 0.4)

    ax.set_title(title, fontsize=font_size)
    ax.set(xlabel=xlabel, ylabel=ylabel)

    plt.rc('axes', titlesize=title_size)    # fontsize of the axes title
    plt.rc('axes', labelsize=label_size)    # fontsize of the x and y labels
    plt.rc('xtick', labelsize=tick_size)    # fontsize of the tick labels
    plt.rc('ytick', labelsize=tick_size)    # fontsize of the tick labels

    ax.legend(dof, loc='best', frameon=True, fontsize=legend_size)

    ax.grid(grid)
    plt.show()
