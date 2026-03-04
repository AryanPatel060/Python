import sys
import gc
import ctypes

def inspect_object(name, obj):
    print(f"--- Inspecting: {name} ---")
    print(f"Value: {obj}")
    print(f"Type:  {type(obj)}")
    print(f"ID:    {id(obj)} (Hex: {hex(id(obj))})")
    # -1 because getrefcount creates its own temporary reference
    print(f"Refs:  {sys.getrefcount(obj) - 1}") 
    print("-" * 25)

# Example Usage
x = [1, 2, 3]
inspect_object("My List", x)

y = x
inspect_object("My List after assignment to y", x)