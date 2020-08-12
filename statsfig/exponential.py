from scipy.stats import expon
import seaborn as sns


def expofig(scale=1, loc=0, size=1000, fig_w=8, fig_l=8, grid=True, color='skyblue', linewidth=15,
            alpha=1, hist=True, xlabel='Exponential Distribution', ylabel='Frequency',
            title='Exponential Distribution', legend_size=12, title_size=20, label_size=16, tick_size=12):
    """

    Exponential Distribution

    parameters
    ----------

    scale: The standard deviation value. The default value is 1. 
    loc: The mean value. The default value is 0.
    size: The Number of random variables. The default value is 1000. 
    fig_w: Matplotlib `figsize` width, the default value is 8.
    fig_l: Matplotlib `figsize` length, the default value is 8.
    grid: Use 'True' or 'False' to show the grid. The default value is True.
    color: The color to fill. The default value is 'skyblue'.
    linewidth: The line width. The default value is 10.
    alpha: The alpha(transparency) value for filling color. The default value is 1.
    hist: Set True to show histogram, otherwise False. The default value is True.
    title: The figure's title. The default value is 'Bernoulli Distribution' 
    xlabel: The x-axis label. The default value is 'Bernoulli Distribution'.
    ylabel: The y-axis label. The default value is 'Frequency'.
    legend_size: The legend font size. The default value is 12.
    title_size: The title font size. The default value is 20.
    label_size: The label font size. The default value is 16.
    tick_size: x and y axis tick font size. The default value is 12.

    Examples
    --------

    import statsfig as sf

    sf.expofig()

    sf.expofig(hist=False, color='#f25acc', size=100)

    """

    plt.figure(figsize=(fig_w, fig_l))

    data_expon = expon.rvs(scale=scale, loc=loc, size=size)

    label = 'scale={}, loc={}, size={}'.format(scale, loc, size)
    ax = sns.distplot(data_expon,
                      kde=True,
                      bins=100,
                      color=color,
                      hist=hist,
                      hist_kws={"linewidth": linewidth, 'alpha': alpha},
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
