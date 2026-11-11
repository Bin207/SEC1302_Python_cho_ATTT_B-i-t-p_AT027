def sol():
    n = input().strip()
    if n[-2:] in ['11', '12', '13']:
        n += "th"
    elif n[-1] == '1':
        n += "st"
    elif n[-1] == '2':
        n += "nd" 
    elif n[-1] == '3':
        n += "rd"
    else:
        n += "th"
    print(''.join(n))
   
def main():
    t = int(input())
    while (t != 0):
        sol()
        t -= 1
    
if __name__ == "__main__":
    main()
