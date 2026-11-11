def sol():
    n = int(input())
    a = {}
    for _ in range(n):
        s = input().split()
        a[s[1]] = s[0]
    
    for ke, va in sorted(a.items()):
        print(f"{ke} -> {va}")
    
def main():
    t = int(input())
    while (t != 0):
        sol()
        t -= 1
    
if __name__ == "__main__":
    main()
