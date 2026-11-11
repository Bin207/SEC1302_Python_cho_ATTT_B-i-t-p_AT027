def sol():
    n = int(input())
    a = list(map(int, input().split()))
    evens = []
    odds = []
    for i in range(len(a)):
        if (a[i] & 1):
            odds.append(a[i])
        else:
            evens.append(a[i])
    combice = evens + odds
    print(*combice)
    sliced = combice[::2]
    print(*sliced)

def main():
    t = int(input())
    while (t != 0):
        sol()
        t -= 1

if __name__ == "__main__":
    main()
