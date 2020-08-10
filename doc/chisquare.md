# Chi-square Distribution

## chifig

### parameters

| Parameter | Default   |                               |
| --------- | --------- | ----------------------------- |
| dof       | [1,4,6,7] | Degree of freedoms to display |
| fig_w     | 8         | Matplotlib `figsize` width    |
| fig_l     | 8         | Matplotlib `figsize` length   |
| grid      | True      | Use 'True' or 'False'         |

### Example

    import statfig as sf
    
    sf.chifig()


![normpdf_std](https://raw.githubusercontent.com/shinokada/statsfig/master/image/chisquare1.png)

```
sf.chifig(dof=[1,4])
```

![normpdf_std](https://raw.githubusercontent.com/shinokada/statsfig/master/image/chisquare2.png)


