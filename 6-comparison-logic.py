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