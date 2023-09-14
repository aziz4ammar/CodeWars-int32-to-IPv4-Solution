def int32_to_ip(int32):
    # Convert the integer to binary representation with 32 bits
    binary_str = bin(int32)[2:].zfill(32)

    # Split the binary string into 4 octets
    octets = [binary_str[i:i+8] for i in range(0, 32, 8)]

    # Convert each octet to decimal and join them with dots to form the IPv4 address
    ipv4_address = ".".join(str(int(octet, 2)) for octet in octets)

    return ipv4_address