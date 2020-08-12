from scipy.stats import gamma
import seaborn as sns


def gammafig(a=5, size=10000, fig_w=8, fig_l=8, grid=True, color='skyblue', linewidth=10,
             alpha=1, hist=True, xlabel='Gamma Distribution', ylabel='Frequency',
             title='Gamma Distribution', legend_size=12, title_size=20, label_size=16,
             tick_size=12):
    """

    Gamma Distribution

    parameters
    ----------

    a: The shape parameter. The default value is 5. 
    size: The Number of random variables. The default value is 1000. 
    fig_w: Matplotlib `figsize` width, the default value is 8.
    fig_l: Matplotlib `figsize` length, the default value is 8.
    grid: Use 'True' or 'False' to show the grid. The default value is True.
    color: The color to fill. The default value is 'skyblue'.
    linewidth: The line width. The default value is 10.
    alpha: The alpha(transparency) value for filling color. The default value is 1.
    title: The figure's title. The default value is 'Bernoulli Distribution' 
    xlabel: The x-axis label. The default value is 'Bernoulli Distribution'.
    ylabel: The y-axis label. The default value is 'Frequency'.
    legend_size: The legend font size. The default value is 12.
    title_size: Title font size. The default value is 20.
    label_size: Label font size. The default value is 16.
    tick_size: x and y axis tick font size. The default value is 12.

    Examples
    --------
    import statsfig as sf

    sf.gammafig()

    sf.gammafig(hist=False, size=1000, color='r')

    """

    fig, ax = plt.subplots(1, 1, figsize=(fig_w, fig_l))

    plt.figure(figsize=(fig_w, fig_l))
    data_gamma = gamma.rvs(a=a, size=size)

    label = 'a={}, size={}'.format(a, size)
    ax = sns.distplot(data_gamma,
                      kde=True,
                      bins=100,
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
