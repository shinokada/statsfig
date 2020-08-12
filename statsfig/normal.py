from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt


def normcdf(x_min=-4, x_max=4, mean=0, std=1, y_max=0.45, xlabel='x', ylabel='pdf(x)', legend_size=12,
            lb=-10, ub=10, font_size=20, alpha=1, fill_color='skyblue', bg_color='white',
            title='Normal Distribution ', fig_w=8, fig_l=8, grid=True, title_size=20, label_size=16,
            tick_size=12):
    """

    Normal Distribution

    parameters
    ----------

    x_min: The x-axis min value. The default value is  -4.
    x_max: The x-axis max value. The default value is  4. 
    mean: The Mean value. The default value is  0 
    std: The Standard deviation value. The default value is  1. 
    y_max: The y-axix max value. The default value is  0.45. 
    xlabel: The x-axis label. The default value is 'x'.
    ylabel: The y-axis label. The default value is 'pdf(x)'. 
    legend_size: The legend font size. The default value is 12.
    lb: The lower bound value. The default value is -10.
    up: The lower bound value. The default value is 10.
    font_size: The title font size. The default value is 20. 
    alpha: Alpha(transparency) value. The default value is 1. 
    fill_color: The filling color. The default value is 'skyblue'.
    bg_color: The background color. If it is not white, it will show the probability. The default value is 'white'.
    title: The figure title. The default value is 'Normal Distribution '.
    fig_w: The Matplotlib `figsize` width. The default value is 8.
    fig_l: The Matplotlib `figsize` length. The default value is  8. 
    grid: Use 'True' or 'False' to show the grid. The default value is 'True'. 
    title_size: The x and y-axis title size. The default value is 20.
    label_size: The label font size. The default value is 16.
    tick_size: The x and y-axis tick size. The default value is 12.

    examples
    --------

    import statfig as sf

    sf.normcdf()

    sf.normcdf(x_min=-4, x_max=10, mean=3, std=2, y_max=0.25,
          xlabel='x', ylabel='pdf(x)', lb=-10, ub=2, font_size=20, alpha=0.5, fill_color='g',
       title='P(X<2) where ', fig_w=10, fig_l=5)

    sf.normcdf(x_min=-4, x_max=10, mean=3, std=2, y_max=0.25,
          xlabel='x', ylabel='pdf(x)', lb=-10, ub=2, font_size=20, fill_color='#73f562', alpha=1,
       bg_color='#f7636f')

    sf.normcdf(mean=1, std=2, lb=0.5, ub=2, y_max=0.25, x_min=-6, x_max=10, bg_color='#fccda7')

    sf.normcdf(mean=3, std=2, lb=4, ub=10, y_max=0.25, x_min=-4, x_max=10)

    """

    fig, ax = plt.subplots(1, 1, figsize=(fig_w, fig_l))
    # for distribution curve
    x = np.arange(x_min, x_max, 0.1)
    ax.plot(x, norm.pdf(x, loc=mean, scale=std), label=None)
    # title
    title = title + ' X~N({}, {}\u00b2)'.format(mean, std, 2)
    ax.set_title(title, fontsize=font_size)

    ax.set(xlabel=xlabel, ylabel=ylabel)

    # probability
    prob = round(norm(mean, std).cdf(ub) - norm(mean, std).cdf(lb), 2)

    # fill background
    # if the background is not white, w or #fff set the label to 1- prob

    prob_com = 1-prob
    bg_prob = 'P(x)=%.2f' % prob_com

    bg_label = None if bg_color == 'white' or bg_color == 'w' or bg_color == '#fff' else bg_prob
    ax.fill_between(x, norm.pdf(x, loc=mean, scale=std),
                    alpha=alpha, color=bg_color, label=bg_label)

    # for fill_between
    px = np.arange(lb, ub, 0.01)
    ax.set_ylim(0, y_max)
    ax.set_xlim(x_min, x_max)
    ax.fill_between(px, norm.pdf(px, loc=mean, scale=std),
                    alpha=alpha, color=fill_color, label='P(x)=%.2f' % prob)

    ax.legend(fontsize=legend_size)

    ax.set_title(title, fontsize=font_size)
    ax.set(xlabel=xlabel, ylabel=ylabel)

    plt.rc('axes', titlesize=title_size)    # fontsize of the axes title
    plt.rc('axes', labelsize=label_size)    # fontsize of the x and y labels
    plt.rc('xtick', labelsize=tick_size)    # fontsize of the tick labels
    plt.rc('ytick', labelsize=tick_size)    # fontsize of the tick labels

    ax.grid(grid)
    plt.show()


def normpdf_std(val=[1, 2, 3, 4], x_min=-4, x_max=4, fig_w=8, fig_l=8, grid=True, xlabel='x', ylabel='pdf(x)',
                title='Normal Distribution', legend_size=12, font_size=20, label_size=16,
                tick_size=12, y_max=0.6, title_size=20):
    """

    Normal Distribution with different standard deviations

    parameters
    ----------

    val: The Degree of freedom values to display. The default value is [1,2,3,4].
    x_min: The x-axis min value. The default value is  -4.
    x_max: The x-axis max value. The default value is  4.
    y_max: The y-axix max value. The default value is  0.45. 
    xlabel: The x-axis label. The default value is 'x'.
    ylabel: The y-axis label. The default value is 'pdf(x)'. 
    legend_size: The legend font size. The default value is 12.
    font_size: The title font size. The default value is 20. 
    title: The figure title. The default value is 'Normal Distribution '.
    fig_w: The Matplotlib `figsize` width. The default value is 8.
    fig_l: The Matplotlib `figsize` length. The default value is  8. 
    grid: Use 'True' or 'False' to show the grid. The default value is 'True'.     
    title_size: The x and y-axis title size. The default value is 20.
    label_size: Label font size. The default value is 16.
    tick_size: The x and y-axis tick size. The default value is 12.


    examples
    --------

    import statfig as sf

    sf.normpdf_std()

    """
    fig, ax = plt.subplots(1, 1, figsize=(fig_w, fig_l))
    x = np.linspace(x_min, x_max, 100)

    for s in val:
        ax.plot(x, norm.pdf(x, scale=s), label='std=%.1f' % s)

    ax.set_ylim(0, y_max)
    ax.set_xlim(x_min, x_max)

    ax.legend(fontsize=legend_size)

    ax.set_title(title, fontsize=font_size)
    ax.set(xlabel=xlabel, ylabel=ylabel)

    plt.rc('axes', titlesize=title_size)    # fontsize of the axes title
    plt.rc('axes', labelsize=label_size)    # fontsize of the x and y labels
    plt.rc('xtick', labelsize=tick_size)    # fontsize of the tick labels
    plt.rc('ytick', labelsize=tick_size)    # fontsize of the tick labels

    ax.grid(grid)

    plt.show()


def normpdf_mean(val=[0, 1, 2, 3], x_min=-10, x_max=10, y_max=0.6, xlabel='x', ylabel='pdf(x)', legend_size=12,
                 font_size=20, title='Normal Distribution', fig_w=8, fig_l=8, grid=True,
                 title_size=20, label_size=16, tick_size=12):
    """

    Normal Distribution with different means

    parameters
    ----------

    val: The Mean values to display. The default value is [0,1,2,3]. 
    x_min: The x-axis min value. The default value is  -10.
    x_max: The x-axis max value. The default value is  10.
    y_max: The y-axix max value. The default value is  0.45. 
    xlabel: The x-axis label. The default value is 'x'.
    ylabel: The y-axis label. The default value is 'pdf(x)'. 
    legend_size: The legend font size. The default value is 12.
    font_size: The title font size. The default value is 20. 
    title: The figure title. The default value is 'Normal Distribution '.
    fig_w: The Matplotlib `figsize` width. The default value is 8.
    fig_l: The Matplotlib `figsize` length. The default value is  8. 
    grid: Use 'True' or 'False' to show the grid. The default value is 'True'.     
    title_size: The x and y-axis title size. The default value is 20.
    label_size: Label font size. The default value is 16.
    tick_size: The x and y-axis tick size. The default value is 12.


    examples
    --------
    import statfig as sf

    sf.normpdf_mean()

     y_max=0.45, xlabel='x', ylabel='pdf(x)', legend_size=12, 
            lb=-10, ub=10, font_size=20, alpha=1, fill_color='skyblue', bg_color='white', 
            title='Normal Distribution ', fig_w=8, fig_l=8,

    """
    fig, ax = plt.subplots(1, 1, figsize=(fig_w, fig_l))
    x = np.linspace(x_min, x_max, 100)

    for mean in val:
        ax.plot(x, norm.pdf(x, loc=mean), label='mean=%.1f' % mean)

    ax.set_ylim(0, y_max)

    ax.legend(fontsize=legend_size)

    ax.set_title(title, fontsize=font_size)
    ax.set(xlabel=xlabel, ylabel=ylabel)

    plt.rc('axes', titlesize=title_size)    # fontsize of the axes title
    plt.rc('axes', labelsize=label_size)    # fontsize of the x and y labels
    plt.rc('xtick', labelsize=tick_size)    # fontsize of the tick labels
    plt.rc('ytick', labelsize=tick_size)    # fontsize of the tick labels

    ax.grid(grid)

    plt.show()
