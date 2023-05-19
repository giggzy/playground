#!/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import random


def initialize(a_, b_, N, R):
    x = np.linspace(0, 10, N)
    y = a_ * x + b_
    for i in range(N):
        y[i] = y[i] + R * (random.random() - 0.5)
    return x, y


# [a_, b_, N, R] = [2, 10, 100, 6]
# x = np.linspace(0, 10, N)
# y = a_ * x + b_
# for i in range(N):
#     y[i] = y[i] + R * (random.random() - 0.5)


def fit_line(x, y, N):
    [SX2, SX, SXY, SY] = [
        sum(x**2),
        sum(x),
        sum(x * y),
        sum(y),
    ]  # Calculate sums of data #

    [M, V] = [
        np.array([[SX2, SX], [SX, N]]),
        np.array([[SXY], [SY]]),
    ]  # Matrix & vector#
    [a, b] = np.dot(np.linalg.inv(M), V)
    y_f = a * x + b  # Matrix equation; fit line #
    return y_f, a, b


# --------------------------- Plot the Results ----------------------------###


def plot_residuals(x, y, y_f, N, a, b):
    plt.subplots(figsize=[8, 4.5])
    plt.scatter(x, y)
    plt.plot(x, y_f)
    for i in range(N):
        plt.plot([x[i], x[i]], [y[i], y_f[i]], ":", color="r", zorder=0)  #
    InfoStr = (
        "Fit: y = " + "{:.5f}".format(float(a)) +
        "x + " + "{:.5f}".format(float(b))
    )  #
    plt.xlabel("x\n" + InfoStr)
    plt.ylabel("y")
    plt.title("Datapoints & Line Fit")

    # Add legend to plot  #
    plt.legend(["${x_i,y_i}$ Data", "Line Fit", "Residuals"])

    plt.show()


def main():
    [a_, b_, N, R] = [2, 10, 100, 17]
    # [a_, b_, N, R] = [33, 550, 100, 55]
    x, y = initialize(a_, b_, N, R)
    # print(f"x: {x}")
    # print(f"y: {y}")

    y_f, a, b = fit_line(x, y, N)
    # print(y_f)

    plot_residuals(x, y, y_f, N, a, b)


if __name__ == "__main__":
    main()
