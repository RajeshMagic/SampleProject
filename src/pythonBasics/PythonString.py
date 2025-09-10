def print_divider(title):
    print("\n" + "="*10 + f" {title} " + "="*10)

# 1. String Creation
print_divider("1. String Creation")
str1 = 'Hello'
str2 = "World"
print(str1, str2)

# 2. Quotes Inside Strings
print_divider("2. Quotes Inside Strings")
print("It's a sunny day")
print('He said, "Hello!"')

# 3. Multiline Strings
print_divider("3. Multiline Strings")
multiline_str = """This is line one
This is line two
This is line three"""
print(multiline_str)

# 4. String Indexing
print_divider("4. String Indexing")
word = "Python"
print(word[0])  # 'P'
print(word[-1]) # 'n'

# 5. String Slicing
print_divider("5. String Slicing")
print(word[1:4])  # 'yth'
print(word[:3])   # 'Pyt'
print(word[3:])   # 'hon'

# 6. String Concatenation
print_divider("6. String Concatenation")
greet = "Hello"
name = "Alice"
full_greet = greet + " " + name
print(full_greet)

# 7. String Repetition
print_divider("7. String Repetition")
laugh = "ha"
print(laugh * 3)

# 8. Length of a String
print_divider("8. Length of a String")
print(len(word))

# 9. Loop Through String
print_divider("9. Loop Through String")
for letter in "apple":
    print(letter)

# 10. Check Substring Presence
print_divider("10. Check Substring Presence")
text = "I love Python programming."
print("Python" in text)  # True
print("Java" not in text)  # True

# 11. String Methods
print_divider("11. String Methods")
text2 = "  Hello, World!  "
print(text2.lower())
print(text2.upper())
print(text2.strip())
print(text2.replace("World", "Python"))
print(text2.split(","))

# 12. String Formatting
print_divider("12. String Formatting")
name2 = "John"
age = 30
print(f"My name is {name2} and I am {age} years old.")

# 13. Escape Characters
print_divider("13. Escape Characters")
print("Line 1\nLine 2")
print("He said, \"Hello!\"")

# 14. Raw Strings
print_divider("14. Raw Strings")
print(r"C:\Users\John")

# 15. Find and Count
print_divider("15. Find and Count")
phrase = "banana"
print(phrase.find("na"))  # 2
print(phrase.count("a"))  # 3

# 16. Startswith and Endswith
print_divider("16. Startswith and Endswith")
filename = "report.pdf"
print(filename.startswith("rep"))
print(filename.endswith(".pdf"))

# 17. Join List into String
print_divider("17. Join List into String")
words = ["Python", "is", "fun"]
sentence = " ".join(words)
print(sentence)





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
