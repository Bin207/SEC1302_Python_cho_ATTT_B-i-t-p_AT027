def sol():
    na = int(input())
    a = {}
    for _ in range(na):
        s = input().split()
        a[s[0]] = a.get(s[0], 0) + int(s[1])
    
    nb = int(input())
    for _ in range(nb):
        s = input().split()
        a[s[0]] = a.get(s[0], 0) + int(s[1])
    
    print(f"Total Unique Items: {len(a)}")
    if a:
        for ke, va in sorted(a.items()):
            print(f"{ke} {va}")
    
def main():
    t = int(input())
    while (t != 0):
        sol()
        t -= 1
    
if __name__ == "__main__":
    main()
