def calculate_crc(data):
    crc = 0xFFFFFFFF
    for byte in data:
        crc ^= byte
        for _ in range(8):
            if crc & 1:
                crc = (crc >> 1) ^ 0xEDB88320
            else:
                crc >>= 1
    return crc ^ 0xFFFFFFFF


def verify_crc(data, crc_value):
    calculated_crc = calculate_crc(data)
    return calculated_crc == crc_value


# Get input from the user
data_to_verify = input("Enter the data to verify: ").encode(
    'utf-8')  # assuming utf-8 encoding for string input
# assuming input is in hexadecimal format
crc_value_to_check = int(input("Enter the CRC value to check: "), 16)

if verify_crc(data_to_verify, crc_value_to_check):
    print("CRC verification successful!")
else:
    print("CRC verification failed!")
