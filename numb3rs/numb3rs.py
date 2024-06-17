import re
import sys

def main():
    user_input_ip = input("IPv4 Address: ").strip()
    is_valid = validate(user_input_ip)
    print(is_valid)

def validate(ip):
    is_valid = re.search(r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$", ip)

    try:
        ip_d1 = int(is_valid[1])
        ip_d2 = int(is_valid[2])
        ip_d3 = int(is_valid[3])
        ip_d4 = int(is_valid[4])
    except TypeError:
        return False
    
    if ip_d1 <= 255 and ip_d2 <= 255 and ip_d3 <= 255 and ip_d4 <= 255:
        return bool(is_valid)
    else:
        return False

if __name__ == "__main__":
    main()
