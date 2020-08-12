# Gamma Distribution

## gammafig()    

### parameters

| Parameters  | Default                  | Description                                      |
| ----------- | ------------------------ | ------------------------------------------------ |
| a           | 5                        | The shape parameter.                             |
| size        | 1000                     | The Number of random variables.                  |
| fig_w       | 8                        | Matplotlib `figsize` width.                      |
| fig_l       | 8                        | Matplotlib `figsize` length.                     |
| grid        | True                     | Use 'True' or 'False' to show the grid.          |
| color       | 'skyblue'                | The color to fill.                               |
| linewidth   | 10                       | The line width size.                             |
| alpha       | 1                        | The alpha(transparency) value for filling color. |
| title       | 'Bernoulli Distribution' | The figure's title.                              |
| xlabel      | 'Bernoulli Distribution' | The x-axis label.                                |
| ylabel      | 'Frequency'              | The y-axis label.                                |
| legend_size | 12                       | The legend font size.                            |
| title_size  | 20                       | The title font size.                             |
| label_size  | 16                       | The label font size.                             |
| tick_size   | 12                       | The x and y axis tick font size.                 |

### Examples

    import statsfig as sf
    
    sf.gammafig()

![gamma1.png](https://raw.githubusercontent.com/shinokada/statsfig/master/image/gamma1.png)

```
sf.gammafig(hist=False, size=1000, color='r')
```

![gamma2.png](https://raw.githubusercontent.com/shinokada/statsfig/master/image/gamma2.png)