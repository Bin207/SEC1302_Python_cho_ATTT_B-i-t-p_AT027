def sol():
    k, m = map(int, input().split())
    au = {}
    dy = {}
    for _ in range(k):
        s = input().split()
        au[s[0]] = s[1]
        
    for _ in range(m):
        s = input().split()
        if s[0] in au:
            if au[s[0]] == s[1]:
                print(f"PASS: {s[0]} -> {au[s[0]]}")
            else:
                print(f"ALERT: CACHE POISONING FOR {s[0]} ({au[s[0]]} != {s[1]})")
        else:
            if s[0] not in dy:
                dy[s[0]] = s[1]
                print(f"LEARNED: {s[0]} -> {dy[s[0]]}")
            else:
                if dy[s[0]] == s[1]:
                    print(f"PASS: {s[0]} -> {dy[s[0]]}")
                else:
                    print(f"ALERT: DYNAMIC CONFLICT FOR {s[0]} ({dy[s[0]]} != {s[1]})")
    
def main():
    t = int(input())
    while (t != 0):
        sol()
        t -= 1
    
if __name__ == "__main__":
    main()
