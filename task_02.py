import scipy.integrate as spi
from monte_carlo import monte_carlo
from plot import plot
from function import fn

if __name__ == "__main__":
    a = 0
    b = 3
    num_samples_1 = 10000
    num_samples_2 = 100000

    plot(fn, a, b)

    area_under_curve_1 = monte_carlo(fn, a, b, num_samples_1)

    print(
        "Calculated using Monte Carlo with {} samples: {}".format(
            num_samples_1, area_under_curve_1
        )
    )

    area_under_curve_2 = monte_carlo(fn, a, b, num_samples_2)
    print(
        "Calculated using Monte Carlo with {} samples: {}".format(
            num_samples_2, area_under_curve_2
        )
    )

    result, error = spi.quad(fn, a, b)
    print("Math calculation: ", result)
