def sol():
    n = int(input())
    a = list(map(int, input().split())) 
        
    print(*sorted(a))
    print(*sorted(a, reverse = True))
    print(*a[::-1])

def main():
    t = int(input())
    while (t != 0):
        sol()
        t -= 1
    
if __name__ == '__main__':
    main()
