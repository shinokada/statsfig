import seaborn as sns
from scipy.stats import binom


def binofig(num=20, prob=0.5, loc=0, size=1000, fig_w=8, fig_l=8, grid=True):
    """

    parameters
    ----------
    num: number of trials
    prob: probability of a success on an individual trial
    loc: location parameter
    size: number of random variables
    fig_w: default: 8, Matplotlib `figsize` width
    fig_l: default: 8, Matplotlib `figsize` length
    grid: default True, Use 'True' or 'False'

    example
    -------
    import statsfig as sf

    sf.binofig()

    sf.binofig(size=100, grid=False)

    """

    plt.figure(figsize=(fig_w, fig_l))

    data_binom = binom.rvs(n=num, p=prob, loc=loc, size=size)

    ax = sns.distplot(data_binom,
                      kde=True,
                      color='skyblue',
                      hist_kws={"linewidth": 10, 'alpha': 1},
                      hist=False
                      )
    ax.set(xlabel='Binomial Distribution', ylabel='Frequency')
    ax.grid(grid)
    plt.show()
