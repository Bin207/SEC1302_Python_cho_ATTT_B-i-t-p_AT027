def sol():
    n, q = map(int, input().split())
    a = {}
    
    for _ in range(n):
        s = input().split()
        a[s[0]] = s[1]
    
    for _ in range(q):
        s = input()
        print(a.get(s, "NOT_FOUND"))
    
def main():
    t = int(input())
    while (t != 0):
        sol()
        t -= 1
    
if __name__ == "__main__":
    main()
