# Shopping cart example

# Shopping cart full of numbers (a Python list of numbers)
cart = [5, 7, 9, 10, 12, 15, 19, 20, 22]

cashier = [] # the cashier starts with zero items
for item in cart: # go over each item one by one
    cashier.append(item) # hand the cashier each item
print(cashier)

cart

"""Now how could you make this shorter?  Could you do it in one line of code instead of three?
This is where list comprehensions come into play.
Let's check using a different cashier to make sure."""

cashier_2 = [item for item in cart]

"""Wait?  Surely this can't be the same as the lines above?
Let's check."""

print(cashier)
print(cashier_2)

"""They're exactly the same!"""

# Some more shopping cart examples

# Only give cashier_3 even numbers
cashier_3 = []
for item in cart:
    if item % 2 == 0:
        cashier_3.append(item)
print(cashier_3)

cashier_3 = [item for item in cart if item % 2 == 0]
print(cashier_3)


# Cashier 4 example; only give cashier 4 odd numbers over 100
cashier_4 = []
for item in cart:
    item += 100 # add 100 to each item to bring them over 100
    if item % 2 == 1: # check to see if they're odd or not
        cashier_4.append(item)
print(cashier_4)

# Now let's try it with list comprehension
cashier_4 = [item+100 for item in cart if item % 2 == 1]
print(cashier_4)


# Now let's see if we can push this.