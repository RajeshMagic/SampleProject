# ===============================================================
# PYTHON REGEX (Regular Expressions) - DEMONSTRATION
# ===============================================================
# RegEx = Regular Expressions
# - Sequence of characters that form a search pattern.
# - Used for searching, matching, and manipulating strings.
#
# Python provides 're' module for regex.
#
# Main Functions:
#   re.findall() -> returns all matches as a list
#   re.search()  -> returns first match as Match object
#   re.split()   -> splits string by regex
#   re.sub()     -> replaces matches
#
# Match object provides:
#   .span()   -> start and end position of match
#   .string   -> original string
#   .group()  -> matched substring
# ===============================================================

import re

txt = "The rain in Spain"

print("\n==============================")
print(" 1. BASIC SEARCH USING PATTERN ")
print("==============================")
x = re.search("^The.*Spain$", txt)
print(f"Does '{txt}' start with 'The' and end with 'Spain'? ->", bool(x))
print("Important Note: ^ means start, $ means end.\n")


print("==============================")
print(" 2. FINDALL() FUNCTION ")
print("==============================")
print("Find all 'ai' in text:", re.findall("ai", txt))
print("Find 'Portugal' in text:", re.findall("Portugal", txt))
print("Important Note: If no matches are found, returns an empty list.\n")


print("==============================")
print(" 3. SEARCH() FUNCTION ")
print("==============================")
match = re.search(r"\s", txt)
print("First whitespace located at position:", match.start())
print("Search for 'Portugal':", re.search("Portugal", txt))
print("Important Note: search() returns Match object or None.\n")


print("==============================")
print(" 4. SPLIT() FUNCTION ")
print("==============================")
print("Split text by whitespace:", re.split(r"\s", txt))
print("Split with maxsplit=1:", re.split(r"\s", txt, 1))
print("Important Note: split() breaks the string at regex pattern.\n")


print("==============================")
print(" 5. SUB() FUNCTION ")
print("==============================")
print("Replace spaces with 9:", re.sub(r"\s", "9", txt))
print("Replace first 2 spaces with 9:", re.sub(r"\s", "9", txt, 2))
print("Important Note: sub() replaces regex matches with given text.\n")


print("==============================")
print(" 6. MATCH OBJECT DEMO ")
print("==============================")
x = re.search("ai", txt)
print("Match object:", x)
print("Span (start,end):", x.span())
print("Original string:", x.string)
print("Matched text:", x.group())

y = re.search(r"\bS\w+", txt)  # Word starting with uppercase 'S'
print("\nAnother regex (word starting with 'S'):")
print("Span:", y.span())
print("String:", y.string)
print("Group:", y.group())
print("Important Note: Match object is powerful for extracting details.\n")


print("==============================")
print(" 7. METACHARACTERS DEMO ")
print("==============================")
demo_txt = "hello planet 123"
print("'.' Any char ->", re.findall("he..o", demo_txt))
print("^ Start ->", re.findall("^hello", demo_txt))
print("$ End ->", re.findall("123$", demo_txt))
print("* Zero/more ->", re.findall("he.*o", demo_txt))
print("+ One/more ->", re.findall("he.+o", demo_txt))
print("? Zero/one ->", re.findall("he.?o", demo_txt))
print("{2} Exactly count ->", re.findall("he.{2}o", demo_txt))
print("| Either/or ->", re.findall("hello|planet", demo_txt))
print("Important Note: Metacharacters define flexible search rules.\n")


print("==============================")
print(" 8. SPECIAL SEQUENCES DEMO ")
print("==============================")
demo_txt = "The rain in Spain 123"
print(r"\A Start of string ->", re.findall(r"\AThe", demo_txt))
print(r"\b Word boundary ->", re.findall(r"\brain", demo_txt))
print(r"\d Digits ->", re.findall(r"\d", demo_txt))
print(r"\D Non-digits ->", re.findall(r"\D", demo_txt))
print(r"\s Whitespaces ->", re.findall(r"\s", demo_txt))
print(r"\S Non-whitespace ->", re.findall(r"\S", demo_txt))
print(r"\w Word chars ->", re.findall(r"\w", demo_txt))
print(r"\W Non-word chars ->", re.findall(r"\W", demo_txt))
print(r"\Z End of string ->", re.findall(r"123\Z", demo_txt))
print("Important Note: Special sequences simplify regex patterns.\n")


print("==============================")
print(" 9. SETS DEMO ")
print("==============================")
demo_txt = "The rain in Spain 123"
print("[arn] ->", re.findall("[arn]", demo_txt))
print("[a-n] ->", re.findall("[a-n]", demo_txt))
print("[^arn] (not a,r,n) ->", re.findall("[^arn]", demo_txt))
print("[0123] ->", re.findall("[0123]", demo_txt))
print("[0-9] ->", re.findall("[0-9]", demo_txt))
print("[0-5][0-9] (00-59) ->", re.findall("[0-5][0-9]", demo_txt))
print("[a-zA-Z] ->", re.findall("[a-zA-Z]", demo_txt))
print("[+] ->", re.findall("[+]", "2+2=4"))
print("Important Note: Sets allow character ranges and exclusions.\n")


print("==============================")
print(" 10. FLAGS DEMO ")
print("==============================")
demo_txt = "Hello\nHELLO"
print("IGNORECASE:", re.findall("hello", demo_txt, re.IGNORECASE))
print("DOTALL:", re.findall("Hello.*HELLO", demo_txt, re.DOTALL))
print("MULTILINE:", re.findall("^HELLO", demo_txt, re.MULTILINE))
print("Important Note: Flags modify regex behavior (case, multiline, etc.).\n")


print("==============================")
print(" END OF REGEX DEMO ")
print("==============================\n")
