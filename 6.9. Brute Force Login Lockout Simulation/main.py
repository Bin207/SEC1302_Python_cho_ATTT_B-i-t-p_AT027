def sol():
    k, d, m = list(map(int, input().split()))
    cnt = 0
    T_lock = 0
    while m != 0:
        s = input().split()
        timestamp = int(s[0]) 
        status = s[1]
        if T_lock != 0 and timestamp >= T_lock:
            T_lock = 0
            cnt = 0
        
        if T_lock != 0 and timestamp < T_lock:
            print(f"BLOCKED (locked until {T_lock})")
        elif status == "FAILURE":
            cnt += 1
            if (cnt == k):
                T_lock = d + timestamp
                print(f"LOCKOUT_TRIGGERED (locked until {T_lock})")
            else:
                print(f"LOGIN_FAILED ({cnt}/{k})")
        else:
            print("LOGIN_SUCCESS")
            cnt = 0
        m -= 1
    
def main():
    t = int(input())
    for _ in range(t):
        sol()
    
if __name__ == "__main__":
    main()
