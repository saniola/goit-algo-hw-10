import numpy as np


def monte_carlo(fn, a, b, num_samples):
    x_random = np.random.uniform(a, b, num_samples)
    y_random = np.random.uniform(0, max(fn(a), fn(b)), num_samples)

    count_under_curve = sum(y_random <= fn(x_random))
    area_rectangle = (b - a) * max(fn(a), fn(b))
    area_under_curve = (count_under_curve / num_samples) * area_rectangle

    return area_under_curve
