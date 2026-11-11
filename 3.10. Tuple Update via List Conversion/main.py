def sol():
    n, q = map(int, input().split())
    a = tuple(map(int, input().split()))
    temp = list(a)
    for _ in range(q):
        i, v = map(int, input().split())
        temp[i] = v
    a = tuple(temp)
    print(*a)
    print(f"Min: {min(a)}, Max: {max(a)}, Sum: {sum(a)}")

def main():
    t = int(input())
    while (t != 0):
        sol()
        t -= 1
    
if __name__ == "__main__":
    main()
