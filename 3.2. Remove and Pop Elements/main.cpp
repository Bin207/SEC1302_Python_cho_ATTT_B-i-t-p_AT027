def sol():
    n = int(input())
    s = input().split()
    target = input()
    if target in s:
        s.remove(target)
    pp_ind = int(input())
    pp = s.pop(pp_ind)
    print(pp)
    print(" ".join(s) if s else "EMPTY")
    

def main():
    t = int(input())
    while (t != 0):
        sol()
        t -= 1

if __name__ == "__main__":
    main()
