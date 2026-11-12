class User:
    def __init__(self, first_name, last_name, username, department):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.department = department
    
    def describe_user(self):
        print(f"User {self.username}: {self.first_name.title()} {self.last_name.title()} (Dept: {self.department})")
    
    def greet_user(self):
        print(f"Welcome back, {self.first_name.title()}!")

def main():
    n = int(input())
    for _ in range(n):
        first_name, last_name, username, department = input().split(',')
        user = User(first_name, last_name, username, department)
        user.describe_user()
        user.greet_user()

if __name__ == "__main__":
    main()
