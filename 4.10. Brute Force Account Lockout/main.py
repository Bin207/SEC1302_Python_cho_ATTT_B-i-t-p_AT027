def sol():
    k, m = map(int, input().split())
    cnt_fl = 0
    check = True
    for _ in range(m):
        stt = input()
        if not check:
            print("BLOCKED")
        elif stt == "SUCCESS":
            print("ALLOWED")
            cnt_fl = 0
        elif stt == "FAILURE":
            cnt_fl += 1
            if cnt_fl < k:
                print(f"FAILED {cnt_fl}/{k}")
            else:
                print("LOCKOUT TRIGGERED")
                check = False
    
def main():
    t = int(input())
    while (t != 0):
        sol()
        t -= 1
    
if __name__ == "__main__":
    main()
