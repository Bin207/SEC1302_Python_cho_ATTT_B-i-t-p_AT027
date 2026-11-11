def sol():
    k = int(input())
    acc = []
    while k != 0:
        po = int(input())
        if 1 <= po <= 65535:
            k -= 1
            acc.append(po)
            print(f"ACCEPTED: {po}")
        else:
            print(f"REJECTED: {po}")
    print("Configured Ports: ", *acc)

def main():
    t = int(input())
    for _ in range(t):
        sol()
    
if __name__ == "__main__":
    main()
