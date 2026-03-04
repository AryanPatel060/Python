class Point:
    def __repr__(self):
        return f"this is from repr"
      
    def __str__(self):
	    return "this is str"
    

p = Point()

print(p)
print(repr(p))