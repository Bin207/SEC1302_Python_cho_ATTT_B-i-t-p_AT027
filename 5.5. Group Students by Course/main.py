def sol():
    n = int(input())
    a = {}
    for _ in range(n):
        s = input().split()
        if s[1] not in a:
            a[s[1]] = set()
        a[s[1]].add(s[0])
    
    for i in sorted(a.keys()):
        print(f"{i} ({len(a[i])}):")
        print(*sorted(a[i]))
        
    
def main():
    t = int(input())
    while (t != 0):
        sol()
        t -= 1
    
if __name__ == "__main__":
    main()
