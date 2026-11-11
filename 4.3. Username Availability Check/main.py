def sol():
   n = int(input())
   a = {name.upper() for name in input().split()}
   q = int(input())
   for _ in range(q):
       name = input()
       print("TAKEN" if (name.upper() in a) else "AVAILABLE")
   
def main():
    t = int(input())
    while (t != 0):
        sol()
        t -= 1
    
if __name__ == "__main__":
    main()
