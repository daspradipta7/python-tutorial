from functools import wraps

def log_activity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finish: {func.__name__}")

        return result
    return wrapper

@log_activity
def brew_chai(type, breakfast="samosa"):
    print(f"Brewing {type} chai !!")
    print(f"Having {breakfast} in breakfast !!")


brew_chai("Masala")
brew_chai("Masala",  breakfast="dosa")
