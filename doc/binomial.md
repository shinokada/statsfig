# Binomial Distribution

## binofig

### Parameters

| Parameter   | Default                   |                                                              |
| ----------- | ------------------------- | ------------------------------------------------------------ |
| num         | 20                        | Number of trials                                             |
| p           | 0.5                       | The probability of a success on an individual trial.         |
| loc         | 0                         | The location parameter to shift the graph.                   |
| size        | 1000                      | The Number of random variables.                              |
| fig_w       | 8                         | Matplotlib `figsize` width.                                  |
| fig_l       | 8                         | Matplotlib `figsize` length.                                 |
| grid        | True                      | Use 'True' or 'False' to show the grid. The default value is True. |
| hist        | True                      | To show Histogram, use 'True' or 'False'.                    |
| color       | 'skyblue'                 | The color to fill.                                           |
| linewidth   | 10                        | The line width.                                              |
| alpha       | 1                         | The alpha(transparency) value for filling color.             |
| title       | 'Chi-Square Distribution' | The figure's title.                                          |
| xlabel      | 'Value'                   | The x-axis label.                                            |
| ylabel      | 'Frequency'               | The y-axis label.                                            |
| legend_size | 12                        | The legend font size.                                        |
| title_size  | 20                        | The title font size.                                         |
| label_size  | 16                        | The label font size.                                         |
| tick_size   | 12                        | The x and y axis tick font size.                             |

### Example

```
import statsfig as sf

sf.binofig()
```

![normpdf_std](https://raw.githubusercontent.com/shinokada/statsfig/master/image/binofig1.png)

```
binofig(p=0.7, num=30, loc=1, color='g', linewidth=5)
```

![image-20200812133915609](/Users/shinokada/pythonproject/statsfig/statsfig-python/image/binomial3.png)




```
sf.binofig(size=100, grid=False)
```

![normpdf_std](https://raw.githubusercontent.com/shinokada/statsfig/master/image/binofig2.png)