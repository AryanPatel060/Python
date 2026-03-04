class SuppressErrors:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is ZeroDivisionError:
            print("Caught a division by zero, but we are ignoring it!")
            return True # Swallow the error
        return False # Let any other error crash the program

with SuppressErrors():
    x = 1 / 0 # This won't crash the script!
print("Program continues...")