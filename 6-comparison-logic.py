# Comparison operators
x = 5
y = 10
print(x < y)   # Output: True
print(x > y)   # Output: False
print(x == y)  # Output: False
print(x != y)  # Output: True


# Logical operators
x = 5
y = 10
z = 15
print(x < y and y < z)     # Output: True
print(x < y or y > z)      # Output: True
print(not x < y)           # Output: False

#--------------------------------------------------------------
menu = {"sushi": 12, "pizza": 10, "burger": 8, "salad": 6}
min_price = float('inf')

for item in menu:
    if menu[item] < min_price:
        min_price = menu[item]
        cheapest_item = item

print(f"The cheapest item is {cheapest_item} and its price is {min_price}")

#--------------------------------------------------------------
products = {'apple': 80, 'banana': 100, 'orange': 60, 'strawberry': 30}
for product, amount in products.items():
    if amount == 0:
        print(f"The {product} you requested is currently out of stock.")
    elif amount < 20:
        print(f"Attention, there are only {amount} {product}s left in stock!")
    else:
        print(f"{product} is available in our stock in sufficient quantity.")

print("Inventory tracking completed.")

#--------------------------------------------------------------

my_string = "Hello, World!"
if "World" in my_string:
    print("Found it!")
else:
    print("Not found.")

#--------------------------------------------------------------

x = [1, 2, 3]
y = x
if x is y:
    print("They are the same object!")
else:
    print("They are not the same object.")

#--------------------------------------------------------------

my_bool = True
if not my_bool:
    print("It is false.")
else:
    print("It is true.")

#--------------------------------------------------------------

x = 5
y = 5
if x <= y:
    print("x is less than or equal to y.")
elif x >= y:
    print("x is greater than or equal to y.")
else:
    print("x and y are different.")

#--------------------------------------------------------------

x = 15
if (x >= 0 and x <= 10) or (x >= 20 and x <= 30):
    print("x is within the specified range.")
else:
    print("x is outside the specified range.")

#--------------------------------------------------------------

name = input("What is your name? ")
age = int(input("What is your age? "))

if (age >= 18 and age <= 30) and (name == "Alice" or name == "Bob"):
    print("Welcome, " + name + "!")
else:
    print("Sorry, you are not eligible to enter.")
