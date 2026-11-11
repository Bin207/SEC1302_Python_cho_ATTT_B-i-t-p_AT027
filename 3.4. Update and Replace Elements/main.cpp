def sol():
    n, l, h = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(len(a)):
        a[i] = min(h, max(a[i], l))
    print(*a)
    print(min(a), max(a), "{:.2f}".format(sum(a) / len(a)))
    

def main():
    t = int(input())
    while (t != 0):
        sol()
        t -= 1

if __name__ == "__main__":
    main()
