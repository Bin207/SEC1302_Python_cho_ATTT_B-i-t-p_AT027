def sol():
    n = int(input())
    s = input().lower().split()
    a = {}
    for i in s:
        a[i] = a.get(i, 0) + 1
    
    for na, va in sorted(a.items()):
        print(f"{na} {va}")
    
def main():
    t = int(input())
    while (t != 0):
        sol()
        t -= 1
    
if __name__ == "__main__":
    main()
