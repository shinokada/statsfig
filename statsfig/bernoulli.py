from scipy.stats import bernoulli
import seaborn as sns
from matplotlib import pyplot as plt


def bernofig(p=0.5, size=1000, fig_w=8, fig_l=8, grid=True, color='skyblue', linewidth=15, alpha=1,
             xlabel='Bernoulli Distribution', ylabel='Frequency', title='Bernoulli Distribution',
             legend_size=12, title_size=20, label_size=16, tick_size=12):
    """

    Bernoulli Distribution

    parameters
    ----------

    p: The probability of a success on an individual trial. The default value is 0.5. 
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
    title_size: The title font size. The default value is 20.
    label_size: The label font size. The default value is 16.
    tick_size: The x and y axis tick font size. The default value is 12.

    Examples
    --------
    import statsfig as sf

    sf.bernofig()

    sf.bernofig(p=0.6, color='#2a6bd4', grid=False)

    """

    plt.figure(figsize=(fig_w, fig_l))

    data_bern = bernoulli.rvs(size=size, p=p)

    label = 'p={}, size={}'.format(p, size)
    ax = sns.distplot(data_bern,
                      kde=False,
                      color=color,
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
