# convert any dotted decimal IP address to binary

def IPtoBinary(ip):
    # spliting each part
    octets = ip.split('.')
    # convert each part to binary
    binaryIP = []
    for octet in octets:
        binaryIP.append(bin(int(octet))[2:].zfill(8))
    # join binary
    binaryIP = "".join(binaryIP)
    return binaryIP


if __name__ == '__main__':

    # ip address
    ip = input("Enter IP address: ")

    print(IPtoBinary(ip))
    exit = input("Enter any key to exit")
