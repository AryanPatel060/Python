import CharField
import IntegerField

class Model:
    def __init__(self, **kwargs):
        # Loop through the provided arguments and set them.
        # This will automatically trigger the Descriptor's __set__ method!
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __repr__(self):
        # How do we print beautifully? We dynamically look at the class 
        # to find all the descriptors, then grab their current values.
        cls = self.__class__
        
        # Find all attributes on the class that have a __set__ method (our Fields)
        field_names = [
            name for name, attr in cls.__dict__.items() 
            if hasattr(attr, '__set__')
        ]
        
        # Build a string like: "name='Aryan', age=21"
        kwargs_str = ", ".join(
            f"{name}={getattr(self, name)!r}" for name in field_names
        )
        return f"{cls.__name__}({kwargs_str})"
# --- 1. Define your Schema ---
class User(Model):
    username = CharField(max_length=15)
    email = CharField(max_length=50)
    age = IntegerField(min_value=18)

# --- 2. Test Success ---
print("--- Creating Valid User ---")
user1 = User(username="aryan_p", email="aryan@example.com", age=21)
print(user1) 
# Output: User(username='aryan_p', email='aryan@example.com', age=21)

# --- 3. Test Validation Failures ---
print("\n--- Testing Validations ---")

try:
    # Fails integer validation
    bad_user1 = User(username="admin", email="admin@test.com", age="twenty") 
except TypeError as e:
    print(f"Error Caught: {e}")

try:
    # Fails string length validation
    bad_user2 = User(username="this_username_is_way_too_long", email="test@test.com", age=25)
except ValueError as e:
    print(f"Error Caught: {e}")

try:
    # Fails minimum value validation
    bad_user3 = User(username="kid", email="kid@test.com", age=12)
except ValueError as e:
    print(f"Error Caught: {e}")
