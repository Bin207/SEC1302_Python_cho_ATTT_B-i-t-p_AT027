def sol():
    r = int(input())
    rl = {}
    for _ in range(r):
        st = input().split()
        if st[0] not in rl:
            rl[st[0]] = set()
        for i in range(2, int(st[1]) + 2):
            rl[st[0]].add(st[i])
    
    u = int(input())
    us = {}
    for _ in range(u):
        st = input().split()
        if st[0] not in us:
            us[st[0]] = set()
        for i in range(2, int(st[1]) + 2):
            us[st[0]].add(st[i])
            
    q = int(input())
    for _ in range(q):
        st = input().split()
        if st[0] not in us:
            print("DENIED: USER_NOT_FOUND")
        else:
            if not us[st[0]]:
                print("DENIED: NO_ROLES")
            else:
                kt = False
                for per in us[st[0]]:
                    if st[1] in rl[per]:
                        print("PERMITTED")
                        kt = True
                        break
                
                if not kt:
                    print("DENIED: PERMISSION_DENIED")
    
def main():
    t = int(input())
    while (t != 0):
        sol()
        t -= 1
    
if __name__ == "__main__":
    main()
