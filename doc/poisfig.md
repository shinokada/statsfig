# Poisson Distribution

## poisfig()

### parameters    

| Parameter   | Default   |                                                  |
| ----------- | --------- | ------------------------------------------------ |
| mu          | 4         | The μ value.                                     |
| size        | 1000      | The number of random variables.                  |
| fig_w       | 8         | Matplotlib `figsize` width                       |
| fig_l       | 8         | Matplotlib `figsize` length                      |
| grid        | True      | Use 'True' or 'False'                            |
| hist        | True      | To show Histogram, use 'True' or 'False'.        |
| color       | 'skyblue' | The color to fill.                               |
| linewidth   | 10        | The line width.                                  |
| alpha       | 1         | The alpha(transparency) value for filling color. |
| title       | None      | Figure title                                     |
| xlabel      | 'x'       | x-axis label                                     |
| ylabel      | 'pdf(x)'  | y-axis label                                     |
| legend_size | 12        | The legend font size.                            |
| title_size  | 20        | The x and y-axis title size.                     |
| label_size  | 16        | The label font size.                             |
| tick_size   | 12        | The x and y-axis tick size.                      |

### Example

    import statsfig as sf
    
    sf.poisfig()
![pois1.png](/Users/shinokada/pythonproject/statsfig/statsfig-python/image/pois1.png)



```
sf.poisfig(size=100, grid=False)
```

![pois2.png](/Users/shinokada/pythonproject/statsfig/statsfig-python/image/pois2.png)