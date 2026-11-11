def sol():
    n, q = map(int, input().split())
    dic = {}
    sl = {}
    for _ in range(n):
        s = input().split()
        dic[s[0]] = {"name": s[1], "dept": s[2], "salary": int(s[3])}
        if s[2] not in sl:
            sl[s[2]] = []
        sl[s[2]].append(s[0])
        
    for _ in range(q):
        s = input().split()
        if s[0] == "FIND":
            if s[1] in dic:
                print(f"{dic[s[1]]['name']} {dic[s[1]]['dept']} {dic[s[1]]['salary']}")
            else:
                print("NOT_FOUND")
        else:
            if s[1] in sl:
                avg = 0.0
                for i in sl[s[1]]:
                    avg += dic[i]["salary"]
                print(f"Average Salary in {s[1]}: {(avg / len(sl[s[1]])):.2f}")
            else:
                print("NO_EMPLOYEES_IN_DEPT")
    
def main():
    t = int(input())
    while (t != 0):
        sol()
        t -= 1
    
if __name__ == "__main__":
    main()
