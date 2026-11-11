def sol():
    color = input()
    print("STOP" if color.upper() == "RED" else "CAUTION" if color.upper() == "YELLOW" else "GO" if color.upper() == "GREEN" else "MALFUNCTION")

def main():
    t = int(input())
    while (t != 0):
        sol()
        t -= 1
    
if __name__ == "__main__":
    main()
