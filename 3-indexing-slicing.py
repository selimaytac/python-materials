#Indexing
message = "Hello, World!"
print(message[0])   # Output: "H"
print(message[7])   # Output: "W"

#Slicing

message = "Hello, World!"
print(message[0:5])     # Output: "Hello"
print(message[7:])      # Output: "World!"
print(message[:5])      # Output: "Hello"

#Concatenation
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)    # Output: "John Doe"

# ----------------------------------------------------------------------------
# slicing a string and then concatenating it with another string
message = "Hello, World!"
new_message = message[0:5] + " Python!"
print(new_message)  # Output: Hello Python!

# indexing a list of lists
my_list = [[1, 2], [3, 4], [5, 6]]
print(my_list[1][0])  # Output: 3

# concatenating a list with a repeated element using multiplication
my_list = [1, 2, 3]
new_list = my_list + [4] * 3
print(new_list)  # Output: [1, 2, 3, 4, 4, 4]

#----------------------------------------------------------------------------

string1 = "Python programming is "
string2 = "fun and interesting!"
new_string = string1[:12] + string2[:9]
print(new_string)   # Output: Python programming is fun and 

#----------------------------------------------------------------------------

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
char = "i"
count = 0
for letter in text:
    if letter == char:
        count += 1
print(f"The character '{char}' appears {count} times in the text.")   # Output: The character 'i' appears 6 times in the text.

#----------------------------------------------------------------------------
text = "Python is cool"
reverse_text = text[::-1]
print(reverse_text)   # Output: looc si nohtyP

#----------------------------------------------------------------------------
text = "Python is cool"
words = text.split()
reverse_words = [word[::-1] for word in words]
new_text = " ".join(reverse_words)
print(new_text)   # Output: nohtyP si looc

