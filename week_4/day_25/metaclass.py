import time

class ModelMeta(type):
    # mcs is the metaclass itself. 
    # namespace is the dictionary of methods/variables the developer wrote.
    def __new__(mcs, name, bases, namespace):
        
        # Skip validation for the base 'Model' class
        if name != "Model":
            
            # --- 1. ENFORCE REQUIRED ATTRIBUTES ---
            if "__tablename__" not in namespace:
                # We crash the program at IMPORT TIME!
                raise TypeError(f"Fatal Error: Model '{name}' must define a '__tablename__'")
            
            # --- 2. AUTO-INJECT FIELDS ---
            # We sneak a new attribute into the dictionary before it becomes a class
            print(f"💉 Injecting timestamp field into {name}")
            namespace['auto_timestamp'] = time.time()

        # Forge the class using the modified namespace
        return super().__new__(mcs, name, bases, namespace)



# --- The Base Class ---
class Model(metaclass=ModelMeta):
    pass




class User(Model):
    __tablename__ = "users_table"
    username = "aryan"

print(User.username)        # aryan
print(User.__tablename__)   # users_table
print(User.auto_timestamp)  # 17096... (Injected successfully!)

try:
    class Product(Model):
        price = 99.99
        # Forgot __tablename__!
except TypeError as e:
    print(e) 
# Output: Fatal Error: Model 'Product' must define a '__tablename__'