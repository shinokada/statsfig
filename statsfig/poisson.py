import seaborn as sns
from scipy.stats import poisson

# Poisson


def poisfig(mu=4, size=10000, fig_w=8, fig_l=8, grid=True, hist=True, color='skyblue', linewidth=10,
            alpha=1, title='Poisson Distribution', xlabel='Poisson Distribution', ylabel='Frequency',
            legend_size=12, title_size=20, label_size=16, tick_size=12):
    """

    Poisson Distribution

    parameters
    ----------
    mu: The μ value. The default value is 4.
    size: The number of random variables. The default value is 1000.
    fig_w: Matplotlib `figsize` width, the default value is 8.
    fig_l: Matplotlib `figsize` length, the default value is 8.
    grid: Use 'True' or 'False' to show the grid. The default value is True.
    hist: To show Histogram, use 'True' or 'False'. The default value is True.
    color: The color to fill. The default value is 'skyblue'.
    linewidth: The line width. The default value is 10.
    alpha: The alpha(transparency) value for filling color. The default value is 1.
    title: The figure's title. The default value is 'Poisson Distribution' 
    xlabel: The x-axis label. The default value is 'Poisson Distribution'.
    ylabel: The y-axis label. The default value is 'Frequency'.
    legend_size: The legend font size. The default value is 12.
    title_size: Title font size. The default value is 20.
    label_size: Label font size. The default value is 16.
    tick_size: x and y axis tick font size. The default value is 12. 

    example
    -------
    import statsfig as sf

    sf.poisfig()

    sf.poisfig(size=100, grid=False)

    """
    plt.figure(figsize=(fig_w, fig_l))

    data_binom = poisson.rvs(mu=mu, size=size)

    label = 'mu={}'.format(mu)
    ax = sns.distplot(data_binom,
                      kde=True,
                      color=color,
                      hist_kws={"linewidth": linewidth, 'alpha': alpha},
                      hist=hist,
                      label=label
                      )

    ax.set_title(title)
    ax.set(xlabel=xlabel, ylabel=ylabel)

    ax.legend(fontsize=legend_size)

    plt.rc('axes', titlesize=title_size)    # fontsize of the axes title
    plt.rc('axes', labelsize=label_size)    # fontsize of the x and y labels
    plt.rc('xtick', labelsize=tick_size)    # fontsize of the tick labels
    plt.rc('ytick', labelsize=tick_size)    # fontsize of the tick labels

    ax.grid(grid)

    plt.show()
