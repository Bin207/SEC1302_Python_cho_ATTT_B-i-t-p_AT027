def evaluate_access(user_roles, required_permission, role_permissions_map):
    per = required_permission.split(":", 1)
    
    for role in user_roles:
        perm = role_permissions_map.get(role, set())
        if (required_permission in perm or "*:*" in perm or f"{per[0]}:*" in perm):
            return ("GRANTED", role)
    
    return ("DENIED", "NONE")
    
def main():
    r = int(input())
    role_map = {}
    for _ in range(r):
        ip = input().split()
        role_map[ip[0]] = set(ip[1:])
        
    q = int(input())
    for _ in range(q):
        rl, pe = input().split(" ", 1)
        user_rl = rl.split(",")
        
        status, role = evaluate_access(user_rl, pe, role_map)
        print(f"ACCESS {status} for '{pe}' via [{role}]")

if __name__ == "__main__":
    main()
