import matplotlib.pyplot as plt


def boxplot(info={'bplot 1': [-9, -4, 2, 4, 9], 'bplot 2': [-5, -2, 1, 3, 8], 'bplot 3': [1, 4, 6, 8, 10]},
            vert=True, mycolor=[], fill_color=True, fig_w=8, fig_l=8, grid=True, xlabel='Groups', ylabel='Value',
            title='Box and whisker plot', title_size=20, label_size=16, tick_size=12):
    """

    Box and whisker plot

    parameters
    ----------

    info: Input your label and data in a dictionary form. 
          The default value is 'bplot 1':[-9, -4, 2, 4, 9], 'bplot 2':[-5, -2, 1, 3, 8], 'bplot 3':[1, 4, 6, 8, 10]}
    vert: If True (default), makes the boxes vertical. If False, everything is drawn horizontally.

    fill_color: If False produces boxes with the Line2D artist. Otherwise, boxes and drawn with Patch artists.
                The default vaule is True.
    mycolor: The default colors are ['pink', 'lightblue', 'lightgreen', 'lightsalmon', 'lightseagreen', 'lightgrey'].
             You can add your colors. 
    fig_w: Matplotlib `figsize` width, the default value is 8.
    fig_l: Matplotlib `figsize` length, the default value is 8.
    grid: Use 'True' or 'False' to show the grid. The default value is True.
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
    sf.boxplot()

    info={'bplot 1':[-9, -4, 2, 4, 9]}
    sf.boxplot(info, mycolor=['skyblue'])

    info={'bplot 1':[-9, -4, 2, 4, 9], 'bplot 2':[-5, -2, 1, 3, 8], 'bplot 3':[1, 4, 6, 8, 10]} 
    sf.boxplot(info, vert=False)

    sf.boxplot(info, vert=False, fill_color=False)

    """

    fig, ax = plt.subplots(1, 1, figsize=(fig_w, fig_l))
    # colors
    l = len(info)
    cols = ['pink', 'lightblue', 'lightgreen',
            'lightsalmon', 'lightseagreen', 'lightgrey']
    if mycolor:
        cols = mycolor+cols

    colors = cols[0:l]
    # destrucure to data and labels from info
    data = []
    labels = []
    for key in info:
        labels.append(key)
        data.append(info[key])

    bplot = ax.boxplot(data,
                       vert=vert,
                       patch_artist=fill_color,
                       labels=labels
                       )

    if fill_color:
        for patch, color in zip(bplot['boxes'], colors):
            patch.set_facecolor(color)

    ax.set_title(title)
    ax.set(xlabel=xlabel, ylabel=ylabel)

    plt.rc('axes', titlesize=title_size)    # fontsize of the axes title
    plt.rc('axes', labelsize=label_size)    # fontsize of the x and y labels
    plt.rc('xtick', labelsize=tick_size)    # fontsize of the tick labels
    plt.rc('ytick', labelsize=tick_size)    # fontsize of the tick labels

    ax.grid(grid)

    plt.show()
