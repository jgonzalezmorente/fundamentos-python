list_numbers = [1, 2, 3, 4, 5, 2, 2, 2]
list_letters = ['a', 'b', 'c']
list_mix = [2, 'z', True, [1, 2, 3], 5.5]

shopping_cart = ['Laptop', 'Sila Gamer', 'Café']

print(type(list_mix))

# Métodos

# Append
print(list_numbers)
list_numbers.append(100)
list_numbers.append(200)
print(list_numbers)

# Remove
list_numbers.remove(4)
list_numbers.remove(100)
print(list_numbers)

# Count
print(list_numbers.count(2))

# .copy()
# .sort()