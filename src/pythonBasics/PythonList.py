# ----------------------------------------
# Python Lists - Complete Demonstration
# ----------------------------------------

print("\n============================")
print(" PYTHON LISTS - DEMONSTRATION ")
print("============================\n")

# 1. Create Lists
print("1. Creating Lists:")
mylist = ["apple", "banana", "cherry"]
print("mylist =", mylist)

list1 = ["abc", 34, True, 40, "male"]
print("Mixed data types list:", list1)

list2 = list(("apple", "banana", "cherry"))
print("Using list() constructor:", list2)

print("\n----------------------------------------")

# 2. Access List Items
print("2. Accessing List Items:")
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print("Full list:", thislist)
print("Item at index 1 ->", thislist[1])
print("Last item (negative index -1) ->", thislist[-1])
print("Items from index 2 to 4 ->", thislist[2:5])
print("Items from beginning to index 3 ->", thislist[:4])
print("Items from index 2 to end ->", thislist[2:])
print("Negative range (-4:-1) ->", thislist[-4:-1])

if "apple" in thislist:
    print("'apple' is present in the list")

print("\n----------------------------------------")

# 3. Change List Items
print("3. Changing List Items:")
thislist = ["apple", "banana", "cherry"]
print("Original:", thislist)

thislist[1] = "blackcurrant"
print("Change second item ->", thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print("Change a range [1:3] ->", thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print("Replace one with two ->", thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print("Replace two with one ->", thislist)

thislist.insert(2, "kiwi")
print("Insert at index 2 ->", thislist)

print("\n----------------------------------------")

# 4. Add List Items
print("4. Adding List Items:")
thislist = ["apple", "banana", "cherry"]
print("Original:", thislist)

thislist.append("orange")
print("Append 'orange' ->", thislist)

thislist.insert(1, "kiwi")
print("Insert 'kiwi' at index 1 ->", thislist)

tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print("Extend with another list:", thislist)

thislist.extend(("grapes", "melon"))
print("Extend with a tuple:", thislist)

print("\n----------------------------------------")

# 5. Remove List Items
print("5. Removing List Items:")
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
print("Original:", thislist)

thislist.remove("banana")
print("Remove first 'banana' ->", thislist)

thislist.pop(1)
print("Pop index 1 ->", thislist)

thislist.pop()
print("Pop last item ->", thislist)

del thislist[0]
print("Delete first item with del ->", thislist)

thislist.clear()
print("Clear all items ->", thislist)

print("\n----------------------------------------")

# 6. Loop Lists
print("6. Looping Through Lists:")
fruits = ["apple", "banana", "cherry"]

print("For loop:")
for x in fruits:
    print("-", x)

print("Loop with index (range & len):")
for i in range(len(fruits)):
    print(f"Index {i} -> {fruits[i]}")

print("While loop:")
i = 0
while i < len(fruits):
    print("-", fruits[i])
    i += 1

print("List comprehension loop:")
[print("-", x) for x in fruits]

print("\n----------------------------------------")

# 7. List Comprehension
print("7. List Comprehension:")
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]
print("Fruits with 'a':", newlist)

newlist = [x.upper() for x in fruits]
print("Upper case fruits:", newlist)

newlist = ['hello' for x in fruits]
print("Replace all with 'hello':", newlist)

newlist = [x if x != "banana" else "orange" for x in fruits]
print("Replace 'banana' with 'orange':", newlist)

print("\n----------------------------------------")

# 8. Sort Lists
print("8. Sorting Lists:")
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
print("Original:", thislist)
thislist.sort()
print("Sorted:", thislist)

thislist.sort(reverse=True)
print("Sorted descending:", thislist)

nums = [100, 50, 65, 82, 23]
nums.sort(key=lambda n: abs(n - 50))
print("Sort by closeness to 50:", nums)

case_list = ["banana", "Orange", "Kiwi", "cherry"]
case_list.sort(key=str.lower)
print("Case-insensitive sort:", case_list)

case_list.reverse()
print("Reversed list:", case_list)

print("\n----------------------------------------")

# 9. Copy Lists
print("9. Copying Lists:")
listA = ["apple", "banana", "cherry"]
listB = listA.copy()
print("Copy using copy() ->", listB)

listC = list(listA)
print("Copy using list() ->", listC)

listD = listA[:]
print("Copy using slice ->", listD)

print("\n----------------------------------------")

# 10. Join Lists
print("10. Joining Lists:")
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print("Using + ->", list3)

list1 = ["a", "b", "c"]
for x in list2:
    list1.append(x)
print("Appending one by one ->", list1)

list1 = ["a", "b", "c"]
list1.extend(list2)
print("Using extend() ->", list1)

print("\n----------------------------------------")

# 11. List Methods
print("11. List Methods Demonstration:")
thislist = ["apple", "banana", "cherry", "apple"]

thislist.append("kiwi")
print("append():", thislist)

count_apple = thislist.count("apple")
print("count('apple') ->", count_apple)

index_banana = thislist.index("banana")
print("index('banana') ->", index_banana)

thislist.insert(1, "mango")
print("insert(1, 'mango') ->", thislist)

thislist.pop(2)
print("pop(2):", thislist)

thislist.remove("apple")
print("remove('apple') ->", thislist)

thislist.reverse()
print("reverse():", thislist)

thislist.sort()
print("sort():", thislist)

copylist = thislist.copy()
print("copy():", copylist)

thislist.clear()
print("clear():", thislist)

print("\n============================")
print(" END OF LIST DEMO ")
print("============================")
