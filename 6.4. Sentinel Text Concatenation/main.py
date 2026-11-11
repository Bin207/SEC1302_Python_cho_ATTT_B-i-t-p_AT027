def sol():
    word = []
    s = ""
    
    while True:
        s = input()
        if s == "END":
            break
        if s == "-":
            continue
        word.append(s)
    
    if word:
        print(' '.join(word))
    else:
        print("EMPTY")
        
    print(f"Words Count: {len(word)}")
    
def main():
    t = int(input())
    for _ in range(t):
        sol()
    
if __name__ == "__main__":
    main()
