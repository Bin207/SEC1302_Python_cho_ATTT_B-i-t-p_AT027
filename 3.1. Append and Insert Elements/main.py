def sol():
    n = int(input())
    s = input().split()
    s.append(input())
    data = input().split()
    pos = int(data[0]) 
    ptr = data[1]
    kq = s[0:pos] + [ptr] + s[pos:]
    print(*kq)
    print(len(kq))
    

def main():
    t = int(input())
    while (t != 0):
        sol()
        t -= 1

if __name__ == "__main__":
    main()
