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
