def calculate_parity_bits(data):
    r = 0
    while (2**r) - 1 < len(data):
        r += 1
    p = []
    for i in range(r):
        p.append(0)
        j = 0
        while j < len(data):
            if (j + 1) & (2**i) != 0:
                p[i] ^= data[j]
            j += 1
    return p


def encode_hamming(data):
    p = calculate_parity_bits(data)
    encoded_data = []
    j = 0
    k = 0
    while j < len(data) + len(p):
        if (j + 1) & (2**k) != 0:
            encoded_data.append(p[k])
            k += 1
        else:
            encoded_data.append(data[j - k])
        j += 1
    return encoded_data


def decode_hamming(data):
    r = 0
    while (2**r) - 1 < len(data):
        r += 1
    syndrome = 0
    for i in range(r):
        for j in range(len(data)):
            if (j + 1) & (2**i) != 0:
                syndrome ^= data[j]
    if syndrome == 0:
        return "No error detected"
    else:
        error_pos = 2**syndrome - 1
        data[error_pos - 1] ^= 1
        return "Error corrected at position:", error_pos - 1


def main():
    data = input("Enter the bit stream: ")
    coded_data = encode_hamming(list(map(int, data)))
    print("Encoded data:", coded_data)

    # Introduce an error (optional)
    coded_data[2] = 1 - coded_data[2]  # Flip a bit for testing

    decoded_data = decode_hamming(coded_data)
    print(decoded_data)


if __name__ == "__main__":
    main()
