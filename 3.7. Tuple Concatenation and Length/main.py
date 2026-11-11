def sol():
    n1 = int(input())
    a = tuple(map(int, input().split()))
    n2 = int(input())
    b = tuple(map(int, input().split()))
    k = int(input())
    c = a + b 
    d = a * k 
    print(*c)
    print(*d)
    print(f"Lengths: {len(c)} {len(d)}")

def main():
    t = int(input())
    while(t != 0):
        sol()
        t -= 1
    
if __name__ == "__main__":
    main()
