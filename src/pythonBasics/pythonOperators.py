# -------------------------------------------
# Python Operators - Full Demonstration
# -------------------------------------------

print("========== PYTHON OPERATORS DEMO ==========\n")

# 1. Arithmetic Operators
print("1. Arithmetic Operators:")
x, y = 15, 4
print(f"x = {x}, y = {y}")
print("x + y  =", x + y)   # Addition
print("x - y  =", x - y)   # Subtraction
print("x * y  =", x * y)   # Multiplication
print("x / y  =", x / y)   # Division
print("x % y  =", x % y)   # Modulus
print("x ** y =", x ** y)  # Exponentiation
print("x // y =", x // y)  # Floor Division
print()

# 2. Assignment Operators
print("2. Assignment Operators:")
x = 10
print("Start: x =", x)
x += 3;  print("x += 3  ->", x)
x -= 2;  print("x -= 2  ->", x)
x *= 4;  print("x *= 4  ->", x)
x /= 3;  print("x /= 3  ->", x)
x %= 5;  print("x %= 5  ->", x)
x = 5
x **= 2; print("x **= 2 ->", x)
x //= 2; print("x //= 2 ->", x)

# Bitwise assignment
x = 5
print("\nBitwise assignments with x=5:")
x &= 3; print("x &= 3  ->", x)
x |= 2; print("x |= 2  ->", x)
x ^= 1; print("x ^= 1  ->", x)
x <<= 2; print("x <<= 2 ->", x)
x >>= 1; print("x >>= 1 ->", x)

# Walrus operator :=
print("\nWalrus Operator (:=):")
print(x := 3)   # assigns and prints at same time
print("x =", x)
print()

# 3. Comparison Operators
print("3. Comparison Operators:")
a, b = 10, 20
print(f"a = {a}, b = {b}")
print("a == b ->", a == b)
print("a != b ->", a != b)
print("a > b  ->", a > b)
print("a < b  ->", a < b)
print("a >= b ->", a >= b)
print("a <= b ->", a <= b)
print()

# 4. Logical Operators
print("4. Logical Operators:")
x, y = True, False
print("x =", x, ", y =", y)
print("x and y ->", x and y)
print("x or y  ->", x or y)
print("not x   ->", not x)
print()

# 5. Identity Operators
print("5. Identity Operators:")
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print("x =", x, "| y =", y, "| z = x")
print("x is z     ->", x is z)       # same object
print("x is y     ->", x is y)       # different objects with same content
print("x == y     ->", x == y)       # values are equal
print("x is not y ->", x is not y)
print()

# 6. Membership Operators
print("6. Membership Operators:")
fruits = ["apple", "banana"]
print("fruits =", fruits)
print("'banana' in fruits     ->", "banana" in fruits)
print("'cherry' not in fruits ->", "cherry" not in fruits)
print()

# 7. Bitwise Operators
print("7. Bitwise Operators:")
x, y = 6, 3
print(f"x = {x} (binary {bin(x)}), y = {y} (binary {bin(y)})")
print("x & y  =", x & y, "->", bin(x & y))  # AND
print("x | y  =", x | y, "->", bin(x | y))  # OR
print("x ^ y  =", x ^ y, "->", bin(x ^ y))  # XOR
print("~x     =", ~x, "->", bin(~x))        # NOT
print("x << 2 =", x << 2, "->", bin(x << 2))# Left shift
print("x >> 2 =", x >> 2, "->", bin(x >> 2))# Right shift
print()

# 8. Operator Precedence
print("8. Operator Precedence:")
print("Example 1: Parentheses first")
print("(6 + 3) - (6 + 3) =", (6 + 3) - (6 + 3))
print("\nExample 2: Multiplication before addition")
print("100 + 5 * 3 =", 100 + 5 * 3)
print("\nExample 3: Left to right with equal precedence (+ and -)")
print("5 + 4 - 7 + 3 =", 5 + 4 - 7 + 3)
print()
print("========== END OF OPERATORS DEMO ==========")
