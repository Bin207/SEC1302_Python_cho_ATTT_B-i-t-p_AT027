def sol():
    Y = int(input())
    s = ""
    if (Y % 400 == 0) or (Y % 4 == 0 and Y % 100 != 0):
        s += "LEAP"
    else:
        s += "COMMON"
    
    if Y % 100 == 0:
        s += " CENTURY"
    else:
        s += " NON-CENTURY"
    
    print(s)
   
def main():
    t = int(input())
    while (t != 0):
        sol()
        t -= 1
    
if __name__ == "__main__":
    main()
