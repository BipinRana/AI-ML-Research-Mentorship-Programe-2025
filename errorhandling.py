
#Error handling
def divide_numbers(a, b):
    """Demonstrate exception handling"""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None
    except TypeError:
        print("Error: Invalid input type!")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None
    finally:
        print("Division operation completed")

#Custom error handling
def validate_age(age):
    """Custom exception example"""
    class InvalidAgeError(Exception):
        pass
    
    try:
        if age < 0:
            raise InvalidAgeError("Age cannot be negative")
        elif age > 150:
            raise InvalidAgeError("Age seems unrealistic")
        return f"Valid age: {age}"
    except InvalidAgeError as e:
        return f"Error: {e}"

print(divide_numbers(10, 2))
print(divide_numbers(10, 0))
print(validate_age(-5))
print(validate_age(25))