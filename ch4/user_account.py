
class UserAccount:
    def __init__(self, username, password):
        self.username = username
        self._password = password
        
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, value):
        self._password = value


user = UserAccount(username="example_user", password="initial_password")
print(user.password)
print(user.username)
