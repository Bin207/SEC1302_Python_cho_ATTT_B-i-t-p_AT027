def main(): 
  t = int(input());

  while (t != 0):
    n = int(input())
    sum = 0

    sum = n * (n + 1) // 2
    
    print(sum)
   
    t -= 1
    
if __name__ == '__main__':
   main()

