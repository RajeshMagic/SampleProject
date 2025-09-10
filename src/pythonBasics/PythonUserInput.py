# ==============================================================
# PYTHON STRING FORMATTING DEMO
# ==============================================================
# String formatting in Python can be done in two main ways:
#  1. f-strings (introduced in Python 3.6) - preferred
#  2. .format() method (older style, still supported)
# ==============================================================

print("\n==============================")
print(" 1. BASIC F-STRINGS ")
print("==============================")

txt = f"The price is 49 dollars"
print(txt)

price = 59
txt = f"The price is {price} dollars"
print(txt)


print("\n==============================")
print(" 2. PLACEHOLDERS & MODIFIERS ")
print("==============================")

price = 59
txt = f"The price is {price:.2f} dollars"  # 2 decimal points
print(txt)

txt = f"The price is {95:.2f} dollars"  # direct value with decimals
print(txt)


print("\n==============================")
print(" 3. OPERATIONS INSIDE F-STRINGS ")
print("==============================")

txt = f"The price is {20 * 59} dollars"  # math inside
print(txt)

price = 59
tax = 0.25
txt = f"The price with tax is {price + (price * tax)} dollars"
print(txt)

price = 49
txt = f"It is very {'Expensive' if price > 50 else 'Cheap'}"
print(txt)


print("\n==============================")
print(" 4. EXECUTING FUNCTIONS INSIDE F-STRINGS ")
print("==============================")

fruit = "apples"
txt = f"I love {fruit.upper()}"  # Using built-in string method
print(txt)

# Custom function inside f-string
def myconverter(x):
    return x * 0.3048

txt = f"The plane is flying at {myconverter(30000)} meters altitude"
print(txt)


print("\n==============================")
print(" 5. MORE MODIFIERS (THOUSAND SEPARATOR, ALIGNMENT, ETC.) ")
print("==============================")

price = 59000
txt = f"The price is {price:,} dollars"   # comma as thousands separator
print(txt)

txt = f"Binary: {255:b}, Hex: {255:X}, Octal: {255:o}"
print(txt)

txt = f"Percentage: {0.85:.0%}"  # percentage format
print(txt)

# Alignment examples
txt = f"Left aligned:  |{'test':<10}|"
print(txt)
txt = f"Right aligned: |{'test':>10}|"
print(txt)
txt = f"Center aligned:|{'test':^10}|"
print(txt)


print("\n==============================")
print(" 6. USING OLD STYLE format() METHOD ")
print("==============================")

price = 49
txt = "The price is {} dollars".format(price)
print(txt)

txt = "The price is {:.2f} dollars".format(price)  # formatted with decimals
print(txt)


print("\n==============================")
print(" 7. MULTIPLE VALUES WITH format() ")
print("==============================")

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))


print("\n==============================")
print(" 8. USING INDEX NUMBERS IN format() ")
print("==============================")

myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))


print("\n==============================")
print(" 9. USING NAMED INDEXES IN format() ")
print("==============================")

myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname="Ford", model="Mustang"))


print("\n==============================")
print(" END OF DEMO ")
print("==============================")
