#List comprehensions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [x**2 for x in numbers]
evens = [x for x in numbers if x % 2 == 0]
odds = [x for x in numbers if x %2 ==1]
nested = [(x,x**2) for x in numbers]

print("Squares:", squares)
print("Even numbers:", evens)
print("Odd numbers:", odds)
print("Nested list:", nested)

# Dictionary comprehensions
word_lengths = {word: len(word) for word in ['apple', 'banana', 'cherry']}
squared_dict = {x: x**2 for x in range(1, 6)}
filtered_dict = {k: v for k, v in squared_dict.items() if v > 10}

print("Word lengths:", word_lengths)
print("Squared dict:", squared_dict)
print("Filtered dict:", filtered_dict)

# Set comprehensions
unique_lengths = {len(word) for word in ['pokhara', 'kathmandu', 'bhaktapur', 'butwal']}
unique_remainders = {x % 3 for x in range(20)}

print("Unique lengths:", unique_lengths)
print("Unique remainders:", unique_remainders)

# Generator comprehensions
squares_gen = (x**2 for x in range(1, 6))
print("Next item in squares: ",next(squares_gen))
print("Next item in squares: ",next(squares_gen))
print("Next item in squares: ",next(squares_gen))
print("Generator squares: ", list(squares_gen))

# Complex comprehension example
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [item for row in matrix for item in row]
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

print("Flattened matrix:", flattened)
print("Transposed matrix:", transposed)
