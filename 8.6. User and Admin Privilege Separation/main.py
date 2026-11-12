class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
    
    def describe_user(self):
        return f"User {self.username} ({self.email})"

class Admin(User):
    def __init__(self, username, email, privileges=None):
        super().__init__(username, email)
        if privileges:
            self.privileges = privileges
        else:
            self.privileges = []
    
    def add_privilege(self, privilege):
        if privilege not in self.privileges:
            self.privileges.append(privilege)
    
    def revoke_privilege(self, privilege):
        if privilege in self.privileges:
            self.privileges.remove(privilege)
            return True
        return False
    
    def show_privileges(self):
        if self.privileges:
            return f"Admin {self.username} privileges: {", ".join(self.privileges)}"
        else:
            return f"Admin {self.username} has no privileges assigned."
    
    def has_privilege(self, privilege):
        return privilege in self.privileges

def main():
    username, email = [x.strip() for x in input().split(',')]
    privilege = input().strip()
    if privilege:
        privilege = [p.strip() for p in privilege.split(',') if p.strip()]
    else:
        privilege = []
    admin = Admin(username, email, privilege)
    
    q = int(input())
    for _ in range(q):
        s = input().strip()
        if s == "INFO":
            print(admin.describe_user())
        elif s == "SHOW":
            print(admin.show_privileges())
        else:
            s = s.split(' ', 1)
            if s[0] == "CHECK":
                print("ALLOWED" if admin.has_privilege(s[1]) else "DENIED", s[1])
            elif s[0] == "REVOKE":
                print("REVOKED" if admin.revoke_privilege(s[1]) else "NOT ASSIGNED", s[1])
            else:
                admin.add_privilege(s[1])

if __name__ == "__main__":
    main()
