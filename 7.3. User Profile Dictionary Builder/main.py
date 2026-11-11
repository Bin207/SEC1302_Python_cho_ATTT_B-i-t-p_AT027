def build_profile(username, role, status='active', email=None):
    profile = {
        'username': username.lower(), 
        'role': role.upper(), 
        'status': status.lower(), 
    }
    
    if email:
        profile['email'] = email
    return profile

def main():
    n = int(input())
    for _ in range(n):
        s = input().split()
        print(build_profile(*s))
        

if __name__ == "__main__":
    main()
