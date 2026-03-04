class CharField:
    def __init__(self, max_length=255):
        self.max_length = max_length

    def __set_name__(self, owner, name):
        self.name = name
        # We store the actual data under a hidden name (e.g., '_username')
        self.private_name = f"_{name}"

    def __get__(self, instance, owner):
        if instance is None:
            return self
        # Retrieve the hidden value from the instance
        return getattr(instance, self.private_name, None)

    def __set__(self, instance, value):
        # 🚨 VALIDATION LOGIC 🚨
        if not isinstance(value, str):
            raise TypeError(f"{self.name} must be a string. Got {type(value).__name__}.")
        if len(value) > self.max_length:
            raise ValueError(f"{self.name} cannot exceed {self.max_length} characters.")
        
        # Save the valid data into the instance's dictionary
        setattr(instance, self.private_name, value)
