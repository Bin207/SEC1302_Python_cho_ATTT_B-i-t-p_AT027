def sol():
    lag = {}
    kt = set()
    cnt = 0
    while True:
        s = input()
        if s == "STOP":
            break;
        s = s.split()
        if s[0] not in kt:
            kt.add(s[0])
            lag[s[1]] = lag.get(s[1], 0) + 1
            cnt += 1
    
    print("Total Valid Votes:", cnt)
    for k, v in sorted(lag.items(), key=lambda x: (-x[1], x[0])):
        print(f"{k}: {v}")
    
def main():
    t = int(input())
    for _ in range(t):
        sol()
    
if __name__ == "__main__":
    main()
