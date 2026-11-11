def sol():
    m = int(input())
    a = {}
    for _ in range(m):
        s = input().split()
        if s[0] == "SET":
            a[s[1]] = s[2]
        elif s[0] == "DEL":
            if s[1] in a:
                del a[s[1]]
        else:
            print(a.get(s[1], "NONE"))
        
    print(f"Total Keys: {len(a)}")
    if not a:
        print("EMPTY")
    else:
        kq = [f"{ke}={va}" for ke, va in sorted(a.items())]
        print(" ".join(kq))
        
    
def main():
    t = int(input())
    while (t != 0):
        sol()
        t -= 1
    
if __name__ == "__main__":
    main()
