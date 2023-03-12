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
