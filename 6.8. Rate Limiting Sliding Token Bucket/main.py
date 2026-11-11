def sol():
    c, r, m = list(map(int, input().split()))
    t_last = 0
    token = c
    for _ in range(m):
        t = int(input())
        delta = t - t_last
        token = min(c, token + delta * r)
        t_last = t
        if token >= 1:
            token -= 1
            print(f"ALLOW (tokens: {token})")
        else:
            print("DROP (rate limit exceeded)")
    
def main():
    t = int(input())
    for _ in range(t):
        sol()
    
if __name__ == "__main__":
    main()
