# If-elif-else statement
score = 85
if score >= 90:
    print("You received an A.")
elif score >= 80:
    print("You received a B.")
elif score >= 70:
    print("You received a C.")
elif score >= 60:
    print("You received a D.")
else:
    print("You failed the course.")

# --------------------------------------------

sentence = input("Enter a sentence: ")
words = sentence.split()
longest_word = ""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word
print("The longest word is:", longest_word)

# --------------------------------------------

num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")

# --------------------------------------------

# A program that prints messages based on user's age and gender

age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ")

if age < 18:
    if gender == "M":
        print("Dear young gentleman, you are not yet of legal age.")
    else:
        print("Dear young lady, you are not yet of legal age.")
elif age >= 18 and age <= 65:
    if gender == "M":
        print("Dear sir, we wish you success in your career.")
    else:
        print("Dear madam, we wish you success in your career.")
else:
    if gender == "M":
        print("Dear sir, we wish you health and happiness in your retirement years.")
    else:
        print("Dear madam, we wish you health and happiness in your retirement years.")

# --------------------------------------------

# A program that decides whether customers who want to eat at a restaurant can be accepted based on their age and hunger level

age = int(input("Please enter your age: "))
hunger_level = int(input("Please enter your hunger level on a scale of 1-10: "))

if age >= 18 and (hunger_level >= 7 or hunger_level <= 2):
    print("Welcome! Please enjoy our restaurant.")
elif age >= 12 and hunger_level >= 5:
    print("Unfortunately, we only serve snacks. You may try another restaurant.")
else:
    print("Sorry, we only accept customers aged 12 and above.") 

# --------------------------------------------

# A program that calculates the final grade of a student based on their exam and project scores

exam_score = int(input("Please enter your exam score: "))
project_score = int(input("Please enter your project score: "))

final_grade = "Fail" if exam_score < 50 or project_score < 50 else "Pass"

print("Your final grade is:", final_grade)
