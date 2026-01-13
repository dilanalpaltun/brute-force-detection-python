import time
import hashlib

class AuthSystem:
    def __init__(self, username, password):
        self.username = username
        self.password_hash = hashlib.sha256(password.encode()).hexdigest()
        self.failed_attempts = {}
        self.login_ban = {}

    def _get_hash(self, text):
        return hashlib.sha256(text.encode()).hexdigest()

    def login(self, user_input, pass_input):
        current_time = time.time()

        if user_input != self.username:
            return "INVALID USERNAME"

        # Check if user is temporarily banned
        if user_input in self.login_ban:
            if current_time < self.login_ban[user_input]:
                remaining = int(self.login_ban[user_input] - current_time)
                return f"PLEASE TRY AGAIN AFTER {remaining} SECONDS."

        # Password check
        if self._get_hash(pass_input) == self.password_hash:
            self.failed_attempts[user_input] = 0
            self.log_event(user_input, "LOGIN SUCCESSFUL")
            return "LOGIN SUCCESSFUL"

        # Failed login
        else:
            self.failed_attempts[user_input] = self.failed_attempts.get(user_input, 0) + 1
            self.log_event(user_input, "LOGIN FAILED")

            # Temporary lock after 5 failed attempts
            if self.failed_attempts[user_input] == 5:
                self.login_ban[user_input] = current_time + 300
                self.log_event(user_input, "ACCOUNT TEMPORARILY LOCKED")
                return "TOO MANY FAILED ATTEMPTS. TRY AGAIN AFTER 5 MINUTES."

            # Brute force detection
            if self.failed_attempts[user_input] > 15:
                self.log_event(user_input, "BRUTE FORCE ATTACK DETECTED")
                return "BRUTE FORCE ATTACK DETECTED"

            return "LOGIN FAILED"

    def log_event(self, user, status):
        with open("auth_security.log", "a") as f:
            f.write(f"{time.ctime()} - User: {user} - Status: {status}\n")


# Example usage
system = AuthSystem("admin", "123456")
print(system.login("admin", "wrong_password"))
