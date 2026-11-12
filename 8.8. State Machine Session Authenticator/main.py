class Authenticator:
    def __init__(self, session_id, max_failures=3, timeout_seconds=300):
        self.session_id = session_id
        self.max_failures = max_failures
        self.timeout_seconds = timeout_seconds
        self.state = "INITIAL"
        self.failed_attempts = 0
        self.created_time = 0
        self.last_activity = 0
    
    def challenge(self, current_time):
        if self.state == "LOCKED":
            return "ACTION_FAILED: SESSION_LOCKED"
        
        if self.state in ("EXPIRED", "AUTHENTICATED"):
            return "ACTION_FAILED: INVALID_STATE"
        
        if current_time - self.last_activity > self.timeout_seconds and self.state != "INITIAL":
            self.state = "EXPIRED"
            return "ACTION_FAILED: SESSION_EXPIRED"
        
        if self.state == "INITIAL":
            self.state = "CHALLENGED"
            self.created_time = current_time
            self.last_activity = current_time
            return "STATE: CHALLENGED"
        else:
            return "STATE: CHALLENGED"
        
    def verify_token(self, token, expected_token, current_time):
        if self.state == "LOCKED":
            return "ACTION_FAILED: SESSION_LOCKED"
        
        if self.state != "CHALLENGED":
            return "ACTION_FAILED: NOT_CHALLENGED"
        
        if current_time - self.last_activity > self.timeout_seconds:
            self.state = "EXPIRED"
            return "ACTION_FAILED: SESSION_EXPIRED"
        
        self.last_activity = current_time
        
        if token == expected_token:
            self.state = "AUTHENTICATED"
            self.failed_attempts = 0
            return "STATE: AUTHENTICATED"
        else:
            self.failed_attempts += 1
            if self.failed_attempts >= self.max_failures:
                self.state = "LOCKED"
                return "STATE: LOCKED"
            return f"VERIFY_FAILED: ATTEMPT {self.failed_attempts}/{self.max_failures}"
    
    def access_resource(self, current_time):
        if self.state == "LOCKED":
            return "DENIED: SESSION_LOCKED"
        
        if self.state != "AUTHENTICATED":
            return "DENIED: NOT_AUTHENTICATED"
        
        if current_time - self.last_activity > self.timeout_seconds:
            self.state = "EXPIRED"
            return "DENIED: SESSION_EXPIRED"
        
        self.last_activity = current_time
        return "GRANTED: ACCESS_OK"
    
    def logout(self):
        if self.state == "LOCKED":
            return "ACTION_FAILED: SESSION_LOCKED"
        
        self.state = "INITIAL"
        return "STATE: INITIAL"

def main():
    session_id, max_failures, timeout_seconds = [x.strip() for x in input().split(',')]
    autor = Authenticator(session_id, int(max_failures), int(timeout_seconds))
    
    q = int(input())
    for _ in range(q):
        tp = input()
        if tp == "LOGOUT":
            print(autor.logout())
        else:
            tp = tp.split()
            if tp[0] == "CHALLENGE":
                print(autor.challenge(int(tp[1])))
            elif tp[0] == "VERIFY":
                print(autor.verify_token(tp[2], tp[3], int(tp[1])))
            else:
                print(autor.access_resource(int(tp[1])))
    
if __name__ == "__main__":
    main()
