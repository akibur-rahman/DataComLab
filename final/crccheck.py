def crc_check(message, crc, generator):

    message += crc

    # Pad the message with 0's equivalent to the degree of the polynomial
    num_zeros = len(generator) - 1
    message += "0" * num_zeros

    rem = message  # Initialize remainder to message
    # Perform modulo 2 division
    for i in range(len(message)):
        if rem[i] == "1":
            rem = xor(rem, generator)  # XOR with generator polynomial
        rem = rem[1:] + "0"

    # If remainder is all 0's, CRC check passes
    if rem == "0" * len(rem):
        return True
    else:
        return False


def xor(a, b):
    ans = ""
    len_a = len(a)
    len_b = len(b)
    max_len = max(len_a, len_b)
    for i in range(max_len):
        bit_a = a[i % len_a]
        bit_b = b[i % len_b]
        if bit_a == bit_b:
            ans += "0"
        else:
            ans += "1"
    return ans


def main():
    message = input("Enter data: ")
    crc = input("Enter CRC code: ")
    generator = input("Enter CRC generator(divisor): ")

    result = crc_check(message, crc, generator)

    if result:
        print("CRC Check Passed")
    else:
        print("CRC Check Failed")


if __name__ == "__main__":
    main()
