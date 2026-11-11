def sol():
    n, target = list(map(int, input().split()))
    a = list(map(int, input().split()))
    cnt = 0
    while target in a:
        a.remove(target)
        cnt += 1
    
    print("Purged Occurrences:", cnt)
    if not a:
        print("Remaining: EMPTY")
    else:
        print("Remaining:", *a)
    
def main():
    t = int(input())
    for _ in range(t):
        sol()
    
if __name__ == "__main__":
    main()
