# for loop: Used to iterate over a sequence (e.g., a list, tuple, string, or range).
# while loop: Used to execute a block of code repeatedly as long as a certain condition is true.

# for loop

for variable in sequence:
    # Code to be executed in each iteration

fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)


# while loop

while condition:
    # Code to be executed in each iteration

i = 1
while i <= 5:
    print(i)
    i += 1

# break statement

for variable in sequence:
    # Code to be executed in each iteration
    if condition:
        break

i = 1
while i <= 5:
    print(i)
    if i == 3:
        break
    i += 1

# continue statement

for variable in sequence:
    # Code to be executed in each iteration
    if condition:
        continue

i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

# else statement

for variable in sequence:
    # Code to be executed in each iteration
    if condition:
        break
else:
    # Code to be executed if the loop ends normally

i = 1
while i <= 5:
    print(i)
    i += 1
else:
    print('i is no longer less than 6')

# range() function

for variable in range(start, stop, step):
    # Code to be executed in each iteration

for i in range(1, 6):
    print(i)

for i in range(1, 6, 2):
    print(i)

# nested loops

for i in range(1, 6):
    for j in range(1, 6):
        print(i, j)

#--------------------------------------------------------------
# Define the employees and their salaries in a dictionary
employees = {'Manager': 20000, 'Accountant': 10000, 'Engineer': 15000, 'Assistant': 7000}

# Define the annual leave entitlement in days for each employee
annual_leave = {'Manager': 30, 'Accountant': 20, 'Engineer': 25, 'Assistant': 15}

# Get input from the user about the employee's name, start year and current year
name = input("Enter employee name: ")
start_year = int(input("Enter start year: "))
current_year = int(input("Enter current year: "))

# Calculate the years of service
years_of_service = current_year - start_year

# Check if the employee exists in the dictionary
if name in employees:
    # Calculate the annual leave entitlement
    leave_entitlement = annual_leave[name] + (years_of_service // 5)

    # Calculate the updated salary with a 10% raise
    updated_salary = employees[name] * 1.1

    # Print the results
    print(f"{name} has worked for {years_of_service} years and is entitled to {leave_entitlement} days of annual leave.")
    print(f"{name}'s updated salary is {updated_salary:.2f} TL.")
else:
    print(f"{name} is not an employee of this company.")

#--------------------------------------------------------------
import random

# Computer generates a random number between 1 and 100
secret_number = random.randint(1, 100)

# User has 3 guesses
num_guesses = 3

while num_guesses > 0:
    # Ask the user to guess a number
    guess = int(input("Guess a number between 1 and 100: "))
    
    # Compare the guess with the secret number
    if guess == secret_number:
        print("Congratulations, you guessed the secret number!")
        break
    elif guess > secret_number:
        print("Try a smaller number.")
    else:
        print("Try a larger number.")
    
    # Decrease the number of remaining guesses
    num_guesses -= 1

# If the user has no guesses left
if num_guesses == 0:
    print(f"Sorry, you lost. The secret number was {secret_number}")
