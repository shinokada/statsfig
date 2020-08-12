import seaborn as sns
from scipy.stats import binom
from matplotlib import pyplot as plt


def binofig(num=20, p=0.5, loc=0, size=1000, fig_w=8, fig_l=8, grid=True, hist=True,
            color='skyblue', linewidth=10, alpha=1, title='Binomial Distribution',
            xlabel='Binomial Distribution', ylabel='Frequency', legend_size=12, title_size=20,
            label_size=16, tick_size=12):
    """

    parameters
    ----------

    num: The number of trials. The default value is 20.
    p: The probability of a success on an individual trial. The default value is 0.5. 
    loc: The Location parameter. The default value is 0. 
    size: The Number of random variables. The default value is 1000. 
    fig_w: Matplotlib `figsize` width, the default value is 8.
    fig_l: Matplotlib `figsize` length, the default value is 8.
    grid: Use 'True' or 'False' to show the grid. The default value is True.
    hist: To show Histogram, use 'True' or 'False'. The default value is True.
    color: The color to fill. The default value is 'skyblue'.
    linewidth: The line width. The default value is 10.
    alpha: The alpha(transparency) value for filling color. The default value is 1.
    title: The figure's title. The default value is 'Chi-Square Distribution' 
    xlabel: The x-axis label. The default value is 'Value'.
    ylabel: The y-axis label. The default value is 'Frequency'.
    legend_size: The legend font size. The default value is 12.
    title_size: The title font size. The default value is 20.
    label_size: The label font size. The default value is 16.
    tick_size: The x and y axis tick font size. The default value is 12. 


    example
    -------
    import statsfig as sf

    sf.binofig()
    sf.binofig(p=0.7, num=30, loc=1, color='g', linewidth=5)
    sf.binofig(size=100, grid=False)

    """

    plt.figure(figsize=(fig_w, fig_l))

    data_binom = binom.rvs(n=num, p=p, loc=loc, size=size)

    label = 'p={}, n={}, loc={}'.format(p, num, loc)
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
