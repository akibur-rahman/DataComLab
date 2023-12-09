import matplotlib.pyplot as plt


def manchester_encode(data):
    encoded_data = []
    for bit in data:
        if bit == '0':
            # Represents a transition from high to low
            encoded_data.extend([1, -1])
        elif bit == '1':
            # Represents a transition from low to high
            encoded_data.extend([-1, 1])
    return encoded_data


def plot_manchester_encoding(data, encoded_data):
    time_values = range(0, 2 * len(data), 2)
    time_values_encoded = [val for pair in zip(
        time_values, time_values) for val in pair][:len(encoded_data)]

    plt.step(time_values_encoded, encoded_data,
             where='post', label='Manchester Encoding')
    plt.xticks(time_values, list(data))
    plt.title('Manchester Encoding')
    plt.xlabel('Time')
    plt.ylabel('Signal Level')
    plt.legend()
    plt.show()


def main():
    user_data = input("Enter binary data (e.g., 101010): ")
    # Remove non-binary characters
    user_data = ''.join(filter(lambda x: x in {'0', '1'}, user_data))

    if not user_data:
        print("Invalid input. Please enter valid binary data.")
        return

    encoded_data = manchester_encode(user_data)
    plot_manchester_encoding(user_data, encoded_data)


if __name__ == "__main__":
    main()
