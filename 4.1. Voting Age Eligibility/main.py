def sol():
    a = int(input())
    print("ELIGIBLE" if a >= 18 else f"INELIGIBLE {18 - a}")

def main():
    t = int(input())
    while (t != 0):
        sol()
        t -= 1
    
if __name__ == "__main__":
    main()
