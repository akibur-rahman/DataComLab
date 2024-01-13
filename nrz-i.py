import matplotlib.pyplot as plt


if __name__ == '__main__':

    input = [0, 1, 1, 0, 0, 1, 0, 1, 1, 1]
    print(input)

sr = []
flag = -1

for bit in input:
    if bit == 0:
        sr.append(flag)
    else:
        flag *= -1
        sr.append(flag)

print(sr)


plt.step(range(len(sr)), sr, where='post')
plt.xlabel('Bit index')
plt.ylabel('Signal Level')
plt.grid(True)
plt.show()
