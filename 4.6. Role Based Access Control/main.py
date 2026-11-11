check = {
    'ADMIN': ['READ', 'WRITE', 'EXECUTE', 'DELETE'],
    'OPERATOR': ['READ', 'WRITE', 'EXECUTE'],
    'AUDITOR': ['READ'],
    'GUEST': []
}

def sol():
    rl, act = input().split()
    if rl not in check:
        print("UNKNOWN ROLE")
    elif act in check[rl]:
        print("PERMITTED")
    else:
        print("DENIED")
    
    
   
def main():
    t = int(input())
    while (t != 0):
        sol()
        t -= 1
    
if __name__ == "__main__":
    main()
