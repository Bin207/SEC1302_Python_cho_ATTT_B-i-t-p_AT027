def sol():
    s = int(input())
    cve = []
    for _ in range(s):
        st = input().split()
        cve.append((st[0], st[1], st[2]))
    
    n = int(input())
    vul = {}
    for _ in range(n):
        st = input().split()
        if st[0] not in vul:
            vul[st[0]] = []
        
        kt = True
        for i in cve:
            if i[0] in st[2]:
                vul[st[0]].append({'po': int(st[1]),'cve' : i[1], 'da' : i[2]})
                kt = False
                break
    
    for ke in vul.keys():
        if len(vul[ke]) == 0:
            print(f"{ke}: SECURE")
        else:
            print(f"{ke} ({len(vul[ke])} vulnerabilities):")
            for va in sorted(vul[ke], key=lambda x: x['po']):
                print(f"Port {va['po']}: {va['cve']} [{va['da']}]")
        
    
def main():
    t = int(input())
    while (t != 0):
        sol()
        t -= 1
    
if __name__ == "__main__":
    main()
