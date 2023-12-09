# Write code for manchester encoding, take data form user. plot graph.

import matplotlib.pyplot as plt
import numpy as np


def manchester(data):
    manchester = []
    for i in range(len(data)):
        if data[i] == 0:
            manchester.append(1)
            manchester.append(-1)
        else:
            manchester.append(-1)
            manchester.append(1)
    return manchester


def plot_graph(data, manchester):
    x = np.arange(0, len(data), 0.5)
    plt.plot(x, data, drawstyle='steps-pre', label='NRZ')
    plt.plot(x, manchester, drawstyle='steps-pre', label='Manchester')
    plt.legend()
    plt.show()


def main():
    data = input("Enter data: ")
    data = list(map(int, data))
    manchester_data = manchester(data)
    plot_graph(data, manchester_data)
