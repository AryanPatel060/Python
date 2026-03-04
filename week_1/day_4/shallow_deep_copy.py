import copy

original = [[1, 2, 3], [4, 5, 6]]

# shallow = copy.copy(original)
shallow = copy.deepcopy(original)

print("Original:", original)
print("Shallow:", shallow)

print(original is shallow)          # False (different outer list)
print(original[0] is shallow[0])    # Fasle (differeent inner list)

shallow[0][0] = 99

print("Original:", original)  #Original: [[1, 2, 3], [4, 5, 6]]
print("Shallow:", shallow)    #Shallow: [[99, 2, 3], [4, 5, 6]]
