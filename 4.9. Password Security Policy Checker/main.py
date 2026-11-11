def checking(blacklisted, username, password):
    kq = []
    if len(password) < 10:
        kq.append("LENGTH")
        
    cnt_up, cnt_lo, cnt_no, cnt_spe = 0, 0, 0, 0
    
    for i in password:
        if i.islower():      
            cnt_lo += 1
        elif i.isupper():    
            cnt_up += 1
        elif i.isdigit():    
            cnt_no += 1
        else:                
            cnt_spe += 1
    if cnt_up == 0 or cnt_lo == 0 or cnt_no == 0 or cnt_spe == 0:
        kq.append("COMPLEXITY")
        
    for i in blacklisted:
        if password.upper() == i:
            kq.append("BLACKLIST")
            break 
    
    if len(username) >= 3:
        for i in range(len(password) - len(username) + 1):
            tam = password[i:len(username)]
            if username.upper() == tam.upper():
                kq.append("USER_CONTAINS")
                break
    
    print("SECURE" if not kq else f"REJECTED: {' '.join(kq)}")


def sol():
    b = int(input())
    bl = input().upper().split()
    us, pw = input().split()
    checking(bl, us, pw)
    
def main():
    t = int(input())
    while (t != 0):
        sol()
        t -= 1
    
if __name__ == "__main__":
    main()
