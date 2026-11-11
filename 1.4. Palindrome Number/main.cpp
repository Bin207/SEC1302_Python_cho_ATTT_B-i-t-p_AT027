def sol():
    s = input()
    le = len(s)
    for i in range(le // 2):
        if s[i] != s[le - 1 - i]:
            print('NO')
            return
    print('YES')

def main():
    t = int(input())
    while (t != 0):
        sol()
        t -= 1

if __name__ == '__main__':
    main()
