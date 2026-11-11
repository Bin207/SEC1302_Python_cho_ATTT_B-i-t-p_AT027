def validate_port(port_num: int) -> tuple[bool, bool]:
    is_valid = 1 <= port_num <= 65535
    is_privileged = is_valid and (1 <= port_num < 1024)
    return is_valid, is_privileged
    

def main():
    n = int(input())
    for _ in range(n):
        po = int(input())
        valid, privileged = validate_port(po)
        if valid and privileged:
            print(f"PORT {po}: VALID PRIVILEGED")
        elif valid and not privileged:
            print(f"PORT {po}: VALID UNPRIVILEGED")
        else:
            print(f"PORT {po}: INVALID")

if __name__ == "__main__":
    main()
