from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt


def normcdf(x_min=-4, x_max=4, mean=0, std=1, y_max=0.45,
            xlabel='x', ylabel='pdf(x)', lb=-10, ub=10, font_size=20, alpha=1, fill_color='skyblue',
            bg_color='white', title='', fig_w=8, fig_l=8, grid=True):
    """

    Normal Distribution

    parameters
    ----------
    x_min: default -4, x-axis min value
    x_max: default 4, x-axis max value
    mean: default 0, Mean value
    std: default 1, Standard deviation value
    y_max: default 0.45, y-axix max value
    xlabel: default 'x', x-axis label
    ylabel: default 'pdf(x)', y-axis label
    lb: default -10, Lower bound
    up: default 10, Upper bound
    font_size: default 20, Font size for title
    alpha: default 1, Alpha(transparency) value
    fill_color: default 'skyblue', Filling color
    bg_color: default 'white', Background color
    title: default None, Figure title
    fig_w: default 8, Matplotlib `figsize` width
    fig_l: default 8, Matplotlib `figsize` length
    grid: default True, Use 'True' or 'False'

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
    title = title + 'X~N({}, {}\u00b2)'.format(mean, std, 2)
    ax.set_title(title, fontsize=font_size)

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(grid)

    # probability
    prob = round(norm(mean, std).cdf(ub) - norm(mean, std).cdf(lb), 2)

    # fill background
    # if the background is not white, w or #fff set the label to 1- prob
    bg_label = None if bg_color == 'white' or bg_color == 'w' or bg_color == '#fff' else 1-prob
    ax.fill_between(x, norm.pdf(x, loc=mean, scale=std),
                    alpha=alpha, color=bg_color, label=bg_label)

    # for fill_between
    px = np.arange(lb, ub, 0.01)
    ax.set_ylim(0, y_max)
    ax.set_xlim(x_min, x_max)
    ax.fill_between(px, norm.pdf(px, loc=mean, scale=std),
                    alpha=alpha, color=fill_color, label=prob)

    ax.legend(fontsize=font_size * 0.7)

    plt.show()


def normpdf_std(val=[1, 2, 3, 4], fig_w=8, fig_l=8, grid=True):
    """

    Normal Distribution with different standard deviations

    parameters
    ----------
    val: default [1,2,3,4], Degree of freedom values
    fig_w: default: 8, Matplotlib `figsize` width
    fig_l: default: 8, Matplotlib `figsize` length
    grid: default True, Use 'True' or 'False'

    examples
    --------
    import statfig as sf

    sf.normpdf_std()

    """
    fig, ax = plt.subplots(1, 1, figsize=(fig_w, fig_l))
    x = np.linspace(-10, 10, 100)
    stdvs = [1, 2, 3, 4]
    for s in stdvs:
        ax.plot(x, norm.pdf(x, scale=s), label='stdv=%.1f' % s)

    ax.set_xlabel('x')
    ax.set_ylabel('pdf(x)')
    ax.set_title('Normal Distribution')
    ax.legend(loc='best', frameon=True)
    ax.set_ylim(0, 0.45)
    ax.grid(True)
    plt.show()


def normpdf_mean(val=[1, 2, 3, 4], fig_w=8, fig_l=8, grid=True):
    """

    Normal Distribution with different means

    parameters
    ----------
    val: default [1,2,3,4], Mean values to display
    fig_w: default: 8, Matplotlib `figsize` width
    fig_l: default: 8, Matplotlib `figsize` length
    grid: default True, Use 'True' or 'False'

    examples
    --------
    import statfig as sf

    sf.normpdf_mean()

    """
    fig, ax = plt.subplots(1, 1, figsize=(fig_w, fig_l))
    x = np.linspace(-10, 10, 100)
    means = val
    for mean in means:
        ax.plot(x, norm.pdf(x, loc=mean), label='mean=%.1f' % mean)

    ax.set_xlabel('x')
    ax.set_ylabel('pdf(x)')
    ax.set_title('Normal Distribution')
    ax.legend(loc='best', frameon=True)
    ax.set_ylim(0, 0.45)
    ax.grid(grid)
    plt.show()
