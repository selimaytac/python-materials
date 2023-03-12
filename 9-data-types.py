# Tuple

# In Python, a tuple is a collection of ordered and immutable elements. 
# Tuples are similar to lists, but unlike lists, tuples cannot be modified once they are created.
# Tuples are represented by parentheses () and individual elements are separated by commas.

# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)

# Accessing elements of a tuple
print(my_tuple[0])  # Output: 1
print(my_tuple[2])  # Output: 3

# Slicing a tuple
print(my_tuple[1:3])  # Output: (2, 3)

# Iterating over a tuple
for element in my_tuple:
    print(element)

# Trying to modify a tuple (this will raise a TypeError)
my_tuple[0] = 10 # Output: TypeError: 'tuple' object does not support item assignment

# Concatenating two tuples
my_tuple2 = (6, 7, 8)
new_tuple = my_tuple + my_tuple2
print(new_tuple)  # Output: (1, 2, 3, 4, 5, 6, 7, 8)

# Set (unordered collection of unique elements)

# In Python, a set is an unordered collection of unique elements.
# Sets are similar to lists and tuples, but unlike lists and tuples, sets cannot contain duplicate elements.
# Sets are represented by curly braces {} or by using the set() function.

# Creating a set
my_set = {1, 2, 3, 4, 5}

# Adding and removing elements from a set
my_set.add(6)
my_set.remove(2)
print(my_set)  # Output: {1, 3, 4, 5, 6}

# Iterating over a set
for element in my_set:
    print(element)

# Removing duplicates from a list using a set
my_list = [1, 2, 3, 2, 4, 5, 1]
new_set = set(my_list)
new_list = list(new_set)
print(new_list)  # Output: [1, 2, 3, 4, 5]

# Checking if two lists have any elements in common
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
set1 = set(list1)
set2 = set(list2)
if set1.intersection(set2):
    print("The two lists have elements in common")
else:
    print("The two lists have no elements in common")

# Dictionary (unordered collection of key-value pairs)

# In Python, a dictionary is an unordered collection of key-value pairs.
# Dictionaries are represented by curly braces {} or by using the dict() function.
# Each key-value pair in a dictionary is separated by a colon : and different key-value pairs are separated by commas.

# Creating a dictionary
my_dict = {"name": "John", "age": 30, "city": "New York"}

# Accessing the values of a dictionary
print(my_dict["name"])  # Output: "John"
print(my_dict["age"])   # Output: 30
print(my_dict["city"])  # Output: "New York"

# Adding and removing key-value pairs from a dictionary
my_dict["gender"] = "Male"
del my_dict["city"]
print(my_dict)  # Output: {"name": "John", "age": 30, "gender": "Male"}

# Iterating over a dictionary
for key, value in my_dict.items():
    print(key, value)

# Iterating over the keys and values of a dictionary
for key in my_dict:
    print(key, my_dict[key])

for value in my_dict.values():
    print(value)
