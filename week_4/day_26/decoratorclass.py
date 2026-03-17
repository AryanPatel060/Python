import time

# --- The Class Decorator ---
def strict_model(cls):
    print(f"Inspecting newly created class: {cls.__name__}")
    
    # 1. Enforce the required attribute
    if not hasattr(cls, "__tablename__"):
        raise TypeError(f"Fatal Error: Model '{cls.__name__}' must define '__tablename__'")
    
    # 2. Inject the auto-timestamp
    print(f"💉 Injecting timestamp into {cls.__name__}")
    cls.auto_timestamp = time.time()
    cls.beta = "teta"
    return cls

# --- The Test Drive ---

# Instead of inheriting from a metaclass, we just decorate it!
@strict_model
class User:
    __tablename__ = "users_table"
    username = "aryan"

print(User.username)        # aryan
print(User.beta)  # 17096... (Successfully injected!)

# If we forgot __tablename__, the decorator would crash it right here.

# here as we can see we have clss which get decorated with the function strict_model tht function is getting cls atgument which is User class itself with this extension we can get the pre processing the class before creating the actual object of User class for that we can use for check if class has reuired method defined or not or we can preinitalize the variable for the class object