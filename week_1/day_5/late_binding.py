multipliers = []

for i in range(5):
    def func(x):
        return x * i
    multipliers.append(func)

# Now, let's call the 'multiply by 2' function (index 2)
print(multipliers[2](10))