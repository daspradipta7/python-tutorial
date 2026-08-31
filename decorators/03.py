from functools import wraps

def check_user_action(func):
    @wraps(func)
    def wrapper(role):
        if (role != "admin"):
            print("Access Denied to role", role)
        else:
            return func(role)

    return wrapper

@check_user_action
def validate_admin_user(role):
    print(f"{role.upper()} role access granted !!!")

validate_admin_user("admin")
validate_admin_user("customer")
