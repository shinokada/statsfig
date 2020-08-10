# Binomial Distribution

## binofig

### Parameters

| Parameter | Default |                                                 |
| --------- | ------- | ----------------------------------------------- |
| num       | 20      | Number of trials                                |
| prob      | 0.5     | Probability of a success on an individual trial |
| loc       | 0       | location parameter                              |
| size      | 1000    | Number of random variables                      |
| fig_w     | 8       | Matplotlib `figsize` width                      |
| fig_l     | 8       | Matplotlib `figsize` length                     |
| grid      | True    | Use 'True' or 'False'                           |
| hist      | True    | Histogram. Use 'True' or 'False'                |

### Example

```
import statsfig as sf

sf.binofig()
```

![normpdf_std](https://raw.githubusercontent.com/shinokada/statsfig/master/image/binofig1.png)


```
sf.binofig(size=100, grid=False)
```

![normpdf_std](https://raw.githubusercontent.com/shinokada/statsfig/master/image/binofig2.png)