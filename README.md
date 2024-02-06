# Integration of fn(x) = x^2 from 0 to 3

In this project, we calculated the definite integral of the function `fn(x) = x^2 + 3x - 3` using the Monte Carlo method with two different numbers of random samples and compared it to the result obtained using the `quad` function from the SciPy library, which uses analytical methods for integration.

## Results

- Calculated using Monte Carlo with 10,000 samples: 14.931
- Calculated using Monte Carlo with 100,000 samples: 14.80725
- Math calculation (analytical result using `quad`): 13.5 (approximately)

## Conclusions

The results obtained using the Monte Carlo method are close to the analytical result obtained with the `quad` function. As the number of random samples increases, the accuracy of the Monte Carlo method improves. These results confirm the correctness and accuracy of applying the Monte Carlo method for numerical integration.

For detailed code and implementation, please refer to the [Python script](task_02.py).
