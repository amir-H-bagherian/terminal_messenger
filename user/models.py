import uuid
import hashlib

class User:
    def __init__(self, username: str, raw_password: str):
        self.user_id = uuid.uuid4()
        self.username = username
        self.password = hashlib.sha256(raw_password.encode()).hexdigest()
        self.is_logged_in = False
        
    def _login_user(self):
        self.is_logged_in = True
    
    def logout_user(self):
        self.is_logged_in = False
    
    def login_status(self):
        return self.is_logged_in
