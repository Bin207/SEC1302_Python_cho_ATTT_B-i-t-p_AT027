def main():
    n = int(input())
    for _ in range(n):
        a = map(int, input().split())
        kq = list(map(lambda x: x * x if x > 0 else abs(x) * 2 if x < 0 else 0, a))
        print(*kq)
        

if __name__ == "__main__":
    main()
