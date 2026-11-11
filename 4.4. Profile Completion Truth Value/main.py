def checking(full_name, login_count, roles):
    kq = []
    if full_name == '-':
        kq.append("NAME")
    if login_count == 0:
        kq.append("LOGINS")
    if roles[0] == '-':
        kq.append("ROLES")
    
    print("ACTIVE" if not kq else f"INCOMPLETE: {' '.join(kq)}")
        

def sol():
   fn = input()
   lg = int(input())
   rl = input().split()
   checking(fn, lg, rl)
   
   
def main():
    t = int(input())
    while (t != 0):
        sol()
        t -= 1
    
if __name__ == "__main__":
    main()
