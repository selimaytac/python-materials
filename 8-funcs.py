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

#--------------------------------------------------------------

import boto3

def create_infrastructure(instance_type):
    ec2 = boto3.resource('ec2')

    # Create a new EC2 instance
    instance = ec2.create_instances(
        ImageId='ami-0c55b159cbfafe1f0',
        InstanceType=instance_type,
        MaxCount=1,
        MinCount=1
    )[0]

    # Wait for the instance to be running
    instance.wait_until_running()

    # Print the public IP address of the instance
    print(instance.public_ip_address)

if __name__ == '__main__':
    # Prompt the user for the instance type to create
    instance_type = input("Enter the instance type to create (e.g. t2.micro): ")

    # Call the create_infrastructure function with the specified instance type
    create_infrastructure(instance_type)

#--------------------------------------------------------------
import logging

def perform_operation(operation):
    # Create a logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Create a file handler for the logger
    file_handler = logging.FileHandler('log.txt')
    file_handler.setLevel(logging.DEBUG)

    # Create a formatter for the log messages
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Add the file handler to the logger
    logger.addHandler(file_handler)

    # Perform the operation and log the result
    try:
        result = operation()
        logger.info('Operation succeeded with result: {}'.format(result))
    except Exception as e:
        logger.error('Operation failed with error: {}'.format(str(e)))

def my_operation():
    # Insert the operation to perform here
    return "Hello, World!"

if __name__ == '__main__':
    perform_operation(my_operation)

#--------------------------------------------------------------

len() # - returns the number of elements in a data structure
print() # - prints the specified arguments to the standard output (usually console)
type() # - returns the type of an object
range() # - returns a sequence of integers in a given range
enumerate() # - allows you to access the elements of a data structure with their indices
zip() # - merges the elements of multiple data structures
sorted() # - sorts a sortable data structure in ascending order
max() # - returns the largest element in a sortable data structure
min() # - returns the smallest element in a sortable data structure
sum() # - returns the sum of the elements in a numerical data structure
round() # - rounds a decimal number to a specified number of decimal places
abs() # - returns the absolute value of a number
all() # - applies a condition to all the elements in a data structure and returns True if all are true, False if at least one is false
any() # - applies a condition to all the elements in a data structure and returns True if at least one is true, False if none are true
filter() # - applies a condition to all the elements in a data structure and returns the elements that meet the condition in a list

# len
my_list = [2, 4, 6, 8, 10]
print("The length of my_list is:", len(my_list))

# output:
# The length of my_list is: 5

# print
my_var = "Hello, world!"
print("The value of my_var is:", my_var)

#output:
# The length of my_list is: 5

# type
my_var = 3.14
print("The type of my_var is:", type(my_var))

# output:
# The type of my_var is: <class 'float'>

# range
for i in range(1, 6):
    print(i)

# output:
# 1
# 2
# 3
# 4
# 5

# enumerate
my_list = [2, 4, 6, 8, 10]
for index, value in enumerate(my_list):
    print("The value at index", index, "is", value)

# output:
# The value at index 0 is 2
# The value at index 1 is 4
# The value at index 2 is 6
# The value at index 3 is 8
# The value at index 4 is 10

my_list2 = ["apple", "banana", "cherry"]
for i, item in enumerate(my_list2):
    print("Index:", i, "Value:", item) 

# output: 
# Index: 0 Value: apple
# Index: 1 Value: banana
# Index: 2 Value: cherry

# zip
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(name, "is", age, "years old.")

# output:
# Alice is 25 years old.
# Bob is 30 years old.
# Charlie is 35 years old.

# sorted
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_list = sorted(my_list)
print("My list:", my_list)
print("Sorted list:", sorted_list)

# output:
# My list: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# Sorted list: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

# max
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print("The maximum value in my_list is:", max(my_list))

# output:
# The maximum value in my_list is: 9

# min
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print("The minimum value in my_list is:", min(my_list))

# output:
# The minimum value in my_list is: 1

# sum
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print("The sum of values in my_list is:", sum(my_list))

# output:
# The sum of values in my_list is: 51

# round
my_float = 3.14159265
print("Rounded value of my_float:", round(my_float, 3))

# output:
# Rounded value of my_float: 3.142

# abs
x = -5
y = abs(x)
print(y) 

# output: 5

# all
my_list = [2, 4, 6, 8]
result = all(num % 2 == 0 for num in my_list)
print(result) 

# output: True

# any
my_list = [2, 4, -6, 8]
result = any(num < 0 for num in my_list)
print(result) 

# output: True

# filter
my_list = [2, 3, 5, 7, 8, 10]
filtered_list = list(filter(lambda x: x <= 5, my_list))
print(filtered_list)

 # output: [2, 3, 5]

 #--------------------------------------------------------------
 # Lambda functions

lambda arguments: expression

add = lambda x, y: x + y
print(add(2, 3)) # Output: 5

numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)

 # Output: [1, 4, 9, 16, 25]

#--------------------------------------------------------------
names = ['John', 'Alice', 'Bob', 'David']
sorted_names = sorted(names, key=lambda x: x.lower())
print(sorted_names)
# output: ['Alice', 'Bob', 'David', 'John']

#--------------------------------------------------------------
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
# output: [2, 4, 6, 8, 10]

#--------------------------------------------------------------
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)
# output: [1, 4, 9, 16, 25]
