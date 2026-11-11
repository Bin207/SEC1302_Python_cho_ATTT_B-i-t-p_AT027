answer = {
    '101' : ['A', 'B', 'B', 'A', 'D', 'C', 'C', 'A', 'B', 'D', 'C', 'C', 'A', 'B', 'D'],
    '102' : ['A', 'C', 'C', 'A', 'B', 'C', 'D', 'D', 'B', 'B', 'C', 'D', 'D', 'B', 'B']
}

def sol():
    s = input().split()
    dapan = s[1:]
    diem = 0.0
    for j in range(len(answer[s[0]])):
        if dapan[j] == answer[s[0]][j]:
            diem += (10 / 15)
    print(f"{diem:.2f}")
    

def main():
    t = int(input())
    while (t != 0):
        sol()
        t -= 1

if __name__ == '__main__':
    main()
