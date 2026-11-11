def simulate_rate_limiter(capacity, refill_rate, request_timestamps, token, last_time):
    return min(token + (request_timestamps - last_time) * refill_rate, capacity)
    
def main():
    ca, rera = map(int, input().split())
    n = int(input())
    token = ca
    last_time = 0
    for _ in range(n):
        t = int(input())
        token = simulate_rate_limiter(ca, rera, t, token, last_time)
        
        if token >= 1:
            token -= 1
            print(f"T={t}: ALLOW (Tokens: {token})")
        else:
            print(f"T={t}: DROP (Tokens: {token})")
        
        last_time = t

if __name__ == "__main__":
    main()
