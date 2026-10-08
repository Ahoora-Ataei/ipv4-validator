import ipaddress

def get_ip_class (first_octet):
    if 1<= first_octet <=126:
        return "A"
    elif first_octet == 127 :
        return"Loopback"
    elif 128<= first_octet <= 191:
        return "B"
    elif 192 <= first_octet <= 223:
        return "C"
    elif 224<= first_octet <= 239:
        return "D (Multicast)"
    elif 240<= first_octet <= 255:
        return "E (Reserved)"
    
try:
    ip_address_input = ipaddress.IPv4Address(input("Enter your IP address : "))
    octets = ip_address_input.packed
    first_octet = octets[0]

    for octet in octets:
        print(f"{octet} = {octet:08b}")


except:
    print("Invalid IPv4 address. Expected format: 0.0.0.0 to 255.255.255.255")


