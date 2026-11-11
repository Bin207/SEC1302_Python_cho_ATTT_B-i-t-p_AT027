def sol():
    s = input()
    for i in s:
        if (i != '0') and (i !='6') and (i != '8'):
            print("NO")
            return
    print("YES") 

def main():
    t = int(input())
    while (t != 0):
        sol()
        t -= 1

if __name__ == '__main__':
        main()
