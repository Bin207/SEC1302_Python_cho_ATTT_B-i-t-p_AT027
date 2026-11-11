def sol():
    n = int(input())
    a = input().split()
    print(f"First: {a[0]}")
    print(f"Last: {a[-1]}")
    print(f"Length: {len(a)}")
    print(f"Single: ('{a[0]}',)")

def main():
    t = int(input())
    while (t != 0):
        sol()
        t -= 1

if __name__ == "__main__":
    main()
