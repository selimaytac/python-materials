def function_name(parameter1, parameter2, ...):
    # Code to be executed
    return output_value


# Function definition
def add_numbers(a, b):
    sum = a + b
    return sum


# Function call
result = add_numbers(5, 10)
print(result)   # Output: 15


# Function definition with parameters
def greet(name, greeting):
    print(f"{greeting}, {name}!")

# Function call with arguments
greet("Alice", "Good morning")

# Function call with keyword arguments
greet(greeting="Hello", name="Bob")


# Function definition with return statement
def add_numbers(x, y):
    result = x + y
    return result

# Function definition with return statement without expression
def print_greeting(name):
    if name:
        print(f"Hello, {name}!")
        return
    print("Hello, world!")
