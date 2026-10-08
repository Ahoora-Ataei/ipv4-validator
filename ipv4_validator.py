import ipaddress
try:
    ip_address_input = ipaddress.IPv4Address(input("Enter your IP address : "))
    octets = ip_address_input.packed

    for octet in octets:
        print(f"{octet} = {octet:08b}")

except:
    print("Invalid IPv4 address. Expected format: 0.0.0.0 to 255.255.255.255")


