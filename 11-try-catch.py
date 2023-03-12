try:
    # Code that might raise an exception
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result: ", result)
except ValueError:
    # Handle the ValueError exception
    print("Please enter a valid integer.")
except ZeroDivisionError:
    # Handle the ZeroDivisionError exception
    print("Cannot divide by zero.")
except Exception as e:
    # Handle any other type of exception
    print("An error occurred:", str(e))
finally:
    # Code that will always run, regardless of whether an exception was thrown
    print("Done.")


# SyntaxError: Raised when there is a syntax error in your code, such as a missing or extra bracket, or an incorrect keyword.

# IndentationError: Raised when the indentation of your code is incorrect, such as when a block of code is not indented correctly.

# NameError: Raised when you try to use a variable or function that has not been defined.

# TypeError: Raised when you try to perform an operation on a value of the wrong type.

# ValueError: Raised when you try to pass an argument to a function that is of the correct type but has an invalid value.

# IndexError: Raised when you try to access an index in a list or other sequence that is out of range.

# KeyError: Raised when you try to access a dictionary key that does not exist.

# FileNotFoundError: Raised when a file or directory does not exist.