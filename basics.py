print("Hello World!")

#Data Types
x = 10          # int
y = 3.14        # float
name = "Alice"  # str
is_active = True # bool
z = None        # NoneType

print(type(x))  # Output: <class 'int'>

a = 10
b = 3
print(a + b)    # Output: 13
print(a // b)   # Output: 3 (floor division)
print(a > b)    # Output: True
print(a is not b)  # Output: True
print("h" in "hello")  # Output: True



text = "Hello, Python!"
print(text[0])       # Output: H
print(text[0:5])     # Output: Hello
print(text.upper())  # Output: HELLO, PYTHON!
print(text.split())  # Output: ['Hello,', 'Python!']
print("Hi" + " there")  # Output: Hi there


name = "Alice"
age = 25
print(f"{name} is {age} years old")  # Output: Alice is 25 years old


x = 10
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")
# Output: Positive


for i in range(3):
    print(i)  # Output: 0, 1, 2



count = 0
while count < 3:
    print(count)
    count += 1  # Output: 0, 1, 2


for i in range(5):
    if i == 3:
        break
    print(i)  # Output: 0, 1, 2


my_list = [1, 2, "apple", 3]
my_list.append(4)      # Add item
print(my_list[2])      # Output: apple
print(my_list)         # Output: [1, 2, 'apple', 3, 4]

my_tuple = (1, 2, "apple")
print(my_tuple[1])     # Output: 2

my_set = {1, 2, 2, 3}
my_set.add(4)
print(my_set)          # Output: {1, 2, 3, 4}

my_dict = {"name": "Alice", "age": 25}
print(my_dict["name"])  # Output: Alice
my_dict["age"] = 26     # Update value
print(my_dict)          # Output: {'name': 'Alice', 'age': 26}


 

def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!

# Default parameter
def add(a, b=10):
    return a + b

print(add(5))       # Output: 15 (uses default b=10)
print(add(5, 3))    # Output: 8

print("Hello", "World", sep=", ", end="!")  # Output: Hello, World!

#Input from user
name = input("Enter your name: ")  
print(f"Hi, {name}")

#Writing
with open("example.txt", "w") as file:
    file.write("Hello, Python!")

#Reading
with open("example.txt", "r") as file:
    content = file.read()
    print(content)  # Prints file content

#Appending
with open("example.txt", "a") as file:
    file.write("\nNew line")