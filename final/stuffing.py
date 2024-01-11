def bit_stuffing(arr):
    stuffed_array = []
    count = 0

    print('Enter the flag:')
    flag = input()

    for bit in arr:
        if bit == '1':
            stuffed_array.append(bit)
            count += 1
            if count == 5:
                stuffed_array.append('0')
                count = 0
        else:
            stuffed_array.append(bit)

    stuffed_array = [flag] + stuffed_array + \
        [flag]  # Use extend to concatenate lists
    return stuffed_array


def bit_destuffing(arr, change_stream):
    destuffed_array = []
    count = 0
    i = 0

    while i < len(arr):
        bit = arr[i]

        if bit == '1':
            destuffed_array.append(bit)
            count += 1

            while i + 1 < len(arr) and arr[i + 1] == '1' and count < 5:
                i += 1
                destuffed_array.append(arr[i])
                count += 1

                if count == 5 and change_stream:
                    i += 1  # Skip the next bit

        else:
            destuffed_array.append(bit)

        i += 1
        # remove flag bits 3 bits
    destuffed_array = destuffed_array[3:-3]

    return destuffed_array


def main():
    # N = 6
    arr = input("Enter the original array (0s and 1s): ")

    print("Original Array:", arr)

    stuffed_array = bit_stuffing(arr)
    print("Stuffed Array:", ''.join(stuffed_array))

    # Option to change transmitted bit stream before destuffing
    change_stream = int(input(
        "Do you want to change the transmitted bit stream before destuffing? (1 for yes, 0 for no): "))

    # Allow the user to change the stuffed data
    if change_stream:
        new_data = input("Enter the new stuffed data (0s and 1s): ")
        arr = new_data

    destuffed_array = bit_destuffing(arr, change_stream)
    print("Destuffed Array:", ''.join(destuffed_array))


if __name__ == "__main__":
    main()
