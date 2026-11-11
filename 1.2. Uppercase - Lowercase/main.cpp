def sol():
    s = input()
    res = ""
    for i in range(len(s)):
        if s[i] >= 'a' and s[i] <= 'z':
            res += s[i].upper()
        elif s[i] >= 'A' and s[i] <= 'Z':
            res += s[i].lower()
        else:
            res += s[i]
    
    print(res)

def main():
    t = int(input())
    while (t != 0):
        sol()
        t -= 1
    
if __name__ == '__main__':
    main()
