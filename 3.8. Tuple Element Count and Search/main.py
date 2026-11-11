def sol():
    n = int(input())
    s = tuple(input().split())
    q = input()
    if q in s:
        print("FOUND")
        print(f"Count: {s.count(q)}")
        print(f"Index: {s.index(q)}")
    else:
        print("NOT FOUND")
        print("Count: 0")

def main():
    t = int(input())
    while (t != 0):
        sol()
        t -= 1

if __name__ == "__main__":
    main()
