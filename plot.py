import numpy as np
import matplotlib.pyplot as plt


def plot(fn, a, b):
    x = np.linspace(a - 0.5, b + 0.5, 400)
    y = fn(x)
    plt.plot(x, y, "r", linewidth=2)
    plt.xlim([x[0], x[-1]])
    plt.ylim([0, max(y) + 0.1])
    plt.xlabel("x")
    plt.ylabel("fn(x)")
    plt.axvline(x=a, color="black", linestyle="--")
    plt.axvline(x=b, color="black", linestyle="--")
    plt.title("Integration of fn(x) = x^2 from {} to {}".format(a, b))
    plt.grid()
    plt.show()
