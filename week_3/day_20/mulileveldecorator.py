from functools import wraps

usernames = ['aryan','smit']

def authenticate(username):
    print(username)
    def admin(func):
        def login(*args,**kwargs):
            print("user authenticated")
            func(*args,**kwargs)
        return login
    
    if username in usernames:
        return admin
    else:
        raise AttributeError(f"{username} is not in the users")

username = "aryan"

@authenticate(username)
def login():
    print("user logged in")

login()