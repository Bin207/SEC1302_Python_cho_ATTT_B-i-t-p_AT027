class User:
    def __init__(self, username, max_allowed_attempts = 3):
        self.username = username
        self.max_allowed_attempts = max_allowed_attempts
        self.login_attempts = 0
        self.is_locked = False
    
    def increment_login_attempts(self):
        self.login_attempts += 1
        if self.login_attempts >= self.max_allowed_attempts:
            self.is_locked = True
            
    def reset_login_attempts(self):
        self.login_attempts = 0
        self.is_locked = False
    
    def get_account_status(self):
        return f"User: {self.username} | Attempts: {self.login_attempts}/{self.max_allowed_attempts} | Locked: {self.is_locked}"

def main():
    username, max_allowed_attempts = [x.strip() for x in input().split(',')]
    user = User(username, int(max_allowed_attempts))
    q = int(input())
    for _ in range(q):
        stt = input()
        if stt == "FAIL":
            user.increment_login_attempts()
            print(f"FAIL RECORDED -> Locked: {user.is_locked}")
        elif stt == "SUCCESS":
            if user.is_locked:
                print("ACCESS DENIED: ACCOUNT LOCKED")
            else:
                user.reset_login_attempts()
                print("LOGIN SUCCESSFUL -> Attempts Reset")
        else:
            print(user.get_account_status())

if __name__ == "__main__":
    main()
