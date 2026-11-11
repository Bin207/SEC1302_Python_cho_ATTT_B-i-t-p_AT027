def sol():
    m_p, m_b = list(map(int, input().split()))
    cal_p = {}
    cal_b = {}
    bl = set()
    while True:
        fl_r = input()
        if fl_r == "END_FLOW":
            break
        fl_r = fl_r.split()
        if fl_r[0] in bl:
            print(f"DROPPED: {fl_r[0]} (ALREADY_BLACKLISTED)")
        else:
            cal_p[fl_r[0]] = cal_p.get(fl_r[0], 0) + 1
            cal_b[fl_r[0]] = cal_b.get(fl_r[0], 0) + int(fl_r[2])
            if cal_p[fl_r[0]] > m_p or cal_b[fl_r[0]] > m_b:
                bl.add(fl_r[0])
                print(f"ALERT: FLOOD DETECTED FROM {fl_r[0]}")
            else:
                print(f"FORWARDED: {fl_r[0]} -> {fl_r[1]} ({fl_r[2]}B)")
    
    if not bl:
        print("Blacklisted Hosts (0): NONE")
    else:
        print(f"Blacklisted Hosts ({len(bl)}):")
        print(' '.join(sorted(bl)))
    
def main():
    t = int(input())
    for _ in range(t):
        sol()
    
if __name__ == "__main__":
    main()
