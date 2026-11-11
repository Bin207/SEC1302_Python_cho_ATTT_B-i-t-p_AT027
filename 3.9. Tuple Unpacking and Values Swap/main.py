def sol():
    n = int(input())
    t = tuple(map(int, input().split()))
    first, *middle, last = t 
    print(f"First: {first}, Last: {last}")
    print(f"Middle Sum: {sum(middle)}")
    new_t = (last, *middle, first)
    print(*new_t)

def main():
    t = int(input())
    while (t != 0):
        sol()
        t -= 1

if __name__ == "__main__":
    main()
    
