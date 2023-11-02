import matplotlib.pyplot as plt


if __name__ == '__main__':
    # take array input
    data = list(map(int, input().split()))
    print(data)

sarray = []

for bit in data:
    if bit == 0:
        sarray.append(-1)
    else:
        sarray.append(1)

    print(sarray)

    # plotting
plt.step(range(len(sarray)), sarray, where='post')
plt.xlabel('Bit index')
plt.ylabel('Signal Level')
plt.grid(True)
plt.show()
