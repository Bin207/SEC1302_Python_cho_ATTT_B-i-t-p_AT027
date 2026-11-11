def sol():
    r = int(input())
    rules = []
    for _ in range(r):
        action, protocol, port_min, port_max = input().split()
        rule_struct = {
        "action": action,
        "protocol": protocol,
        "port_min": int(port_min),
        "port_max": int(port_max)
        }
        rules.append(rule_struct)
    q = int(input())
    for _ in range(q):
        prt, pt = input().split()
        pt = int(pt)
        if not (0 <= pt <= 65535):
            print("INVALID")
        else:
            ktra = False
            for rl in rules:
                if (rl["protocol"] == "ANY" or rl["protocol"] == prt) and (rl["port_min"] <= pt <= rl["port_max"]):
                    print(rl["action"])
                    ktra = True
                    break
            if not ktra:
                print("DENY")
    
def main():
    t = int(input())
    while (t != 0):
        sol()
        t -= 1
    
if __name__ == "__main__":
    main()
