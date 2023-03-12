#Lists
#In Python, a list is a collection of items that can be of any data type, including strings, integers, floats, and even other lists. 
#You can create a list by enclosing a comma-separated sequence of values inside square brackets.

fruits = ["apple", "banana", "cherry"]
print(fruits)    # Output: ["apple", "banana", "cherry"]

#Basic List Operations

#Accessing List Items
fruits = ["apple", "banana", "cherry"]
print(fruits[0])   # Output: "apple"
print(fruits[1])   # Output: "banana"

#Changing List Items
fruits = ["apple", "banana", "cherry"]
fruits[1] = "orange"
print(fruits)    # Output: ["apple", "orange", "cherry"]

#Adding List Items
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)    # Output: ["apple", "banana", "cherry", "orange"]

#Removing List Items
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)    # Output: ["apple", "cherry"]

#--------------------------------------------------------------

my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sum = 0
for sublist in my_list:
    for item in sublist:
        if item % 2 == 0:
            sum += item
print(sum)  # Output: 20 (2 + 4 + 6 + 8)


#--------------------------------------------------------------

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list = []
for item in my_list:
    if item % 2 == 0:
        new_list.append(item**2)
    else:
        new_list.append(item)
print(new_list)  # Output: [1, 4, 3, 16, 5, 36, 7, 64, 9]

#--------------------------------------------------------------

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]
new_list = [x + y + z for x, y, z in zip(list1, list2, list3)]
print(new_list)  # Output: [12, 15, 18]

#--------------------------------------------------------------

my_list = [1, 2, 3, 4, 5]
my_list_reversed = my_list[::-1]
print(my_list_reversed)  # Output: [5, 4, 3, 2, 1]

#--------------------------------------------------------------

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = [item for sublist in list_of_lists for item in sublist]
print(new_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
