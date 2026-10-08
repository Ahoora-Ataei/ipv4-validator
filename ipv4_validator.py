import ipaddress

def get_ip_class (first_octet):
    if first_octet == 0:
        return "0 (Reserved)"
    elif 1<= first_octet <=126:
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
    else:
        return "Unknown"


while True:   
    try:
        raw = input("Enter your IP address : ").strip()
    except EOFError :
        print("\nCancelled.")
        break
    try:
        ip_address_input = ipaddress.IPv4Address(raw)
        octets = ip_address_input.packed
        first_octet = octets[0]

        for octet in octets:
            print(f"{octet} = {octet:08b}")

        print(f"IP class = {get_ip_class(first_octet)}")

    except ipaddress.AddressValueError :
        print("\nInvalid IPv4 address. Expected format: 0.0.0.0 to 255.255.255.255\n")

    try:
        user_choice = input("\nDo you want to continue? (Y)  or  (N) :\n").strip()
    except (EOFError, KeyboardInterrupt):
        print("\nGoodbye!\n")
        break
    
    if user_choice.lower() == "n":
        print("\nGoodbye!\n")
        break
    
