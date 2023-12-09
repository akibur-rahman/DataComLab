# Write code for manchester encoding and decoding, take data form user. plot graph for both.

import matplotlib.pyplot as plt
import numpy as np


def manchester_encode(data):
    encoded_data = []
    for i in range(len(data)):
        if data[i] == 0:
            encoded_data.append(-1)
            encoded_data.append(1)
        else:
            encoded_data.append(1)
            encoded_data.append(-1)
    return encoded_data


def manchester_decode(data):
    decoded_data = []
    for i in range(0, len(data), 2):
        if data[i] == -1 and data[i+1] == 1:
            decoded_data.append(0)
        elif data[i] == 1 and data[i+1] == -1:
            decoded_data.append(1)
        else:
            print("Invalid data")
            return
    return decoded_data


def plot_graph(data, title):
    x = np.arange(0, len(data))
    y = data
    plt.step(x, y, where='post')
    plt.title(title)
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.ylim(-2, 2)
    plt.show()


def main():
    data = list(map(int, input("Enter data: ").split()))
    encoded_data = manchester_encode(data)
    decoded_data = manchester_decode(encoded_data)
    plot_graph(data, "Input data")
    plot_graph(encoded_data, "Manchester encoded data")
    plot_graph(decoded_data, "Manchester decoded data")
