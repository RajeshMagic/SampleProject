# ==============================================================
# PYTHON FILE HANDLING DEMONSTRATION
# ==============================================================
# This program demonstrates:
#   1. Opening files in different modes
#   2. Reading files (full, partial, line by line)
#   3. Writing and appending to files
#   4. Creating new files
#   5. Deleting files and folders
#   6. Best practices (using 'with open()')
# ==============================================================

import os

print("\n==============================")
print(" STEP 0: PREPARE SAMPLE FILE ")
print("==============================")

# Create a sample file "demofile.txt" with initial content
with open("demofile.txt", "w") as f:
    f.write("Hello! Welcome to demofile.txt\n")
    f.write("This file is for testing purposes.\n")
    f.write("Good Luck!\n")

print("Created 'demofile.txt' with sample content.\n")


# ---------------------------------------------------------------
# 1. OPENING AND READING FILES
# ---------------------------------------------------------------
print("\n==============================")
print(" STEP 1: OPENING AND READING FILES ")
print("==============================")

# Open file in read mode (default is 'rt')
with open("demofile.txt") as f:
    print("Reading full file content:")
    print(f.read())

# Read only first 5 characters
with open("demofile.txt") as f:
    print("\nReading only first 5 characters:")
    print(f.read(5))

# Read a single line
with open("demofile.txt") as f:
    print("\nReading single line using readline():")
    print(f.readline(), end="")  # First line
    print(f.readline(), end="")  # Second line

# Loop through all lines
with open("demofile.txt") as f:
    print("\nLooping through all lines in file:")
    for line in f:
        print(line, end="")


# ---------------------------------------------------------------
# 2. CLOSING FILES (Best Practice)
# ---------------------------------------------------------------
print("\n\n==============================")
print(" STEP 2: CLOSING FILES (Best Practice) ")
print("==============================")

# If not using 'with', must manually close the file
f = open("demofile.txt", "r")
print("Reading one line and then closing manually:")
print(f.readline())
f.close()
print("File closed manually. Best practice: always close files!")


# ---------------------------------------------------------------
# 3. WRITING AND APPENDING TO FILES
# ---------------------------------------------------------------
print("\n\n==============================")
print(" STEP 3: WRITING AND APPENDING FILES ")
print("==============================")

# Append content to file ("a")
with open("demofile.txt", "a") as f:
    f.write("This line was appended!\n")

with open("demofile.txt") as f:
    print("After appending:")
    print(f.read())

# Overwrite file completely ("w")
with open("demofile.txt", "w") as f:
    f.write("File content has been overwritten.\n")

with open("demofile.txt") as f:
    print("After overwriting:")
    print(f.read())


# ---------------------------------------------------------------
# 4. CREATING NEW FILES
# ---------------------------------------------------------------
print("\n==============================")
print(" STEP 4: CREATING NEW FILES ")
print("==============================")

# "x" mode creates a file, error if already exists
filename = "myfile.txt"
if not os.path.exists(filename):
    with open(filename, "x") as f:
        f.write("This is a brand new file created with 'x' mode.\n")
    print(f"Created new file '{filename}' using 'x' mode.")
else:
    print(f"File '{filename}' already exists.")

# "a" mode also creates if not exists
with open("myappendfile.txt", "a") as f:
    f.write("File created using 'a' mode.\n")
print("File 'myappendfile.txt' created with append mode.")


# ---------------------------------------------------------------
# 5. DELETING FILES AND FOLDERS
# ---------------------------------------------------------------
print("\n==============================")
print(" STEP 5: DELETING FILES AND FOLDERS ")
print("==============================")

# Safely delete a file
if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")
    print("File 'myfile.txt' deleted.")
else:
    print("File 'myfile.txt' not found.")

# Create and delete a folder
folder_name = "myfolder"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"Folder '{folder_name}' created.")

if os.path.exists(folder_name):
    os.rmdir(folder_name)  # only works if folder is empty
    print(f"Folder '{folder_name}' deleted.")


# ---------------------------------------------------------------
# 6. IMPORTANT NOTES
# ---------------------------------------------------------------
print("\n==============================")
print(" IMPORTANT NOTES ")
print("==============================")
print("1. Modes: 'r'=read, 'w'=write(overwrite), 'a'=append, 'x'=create.")
print("2. Default mode is text 't'; use 'b' for binary (images/files).")
print("3. Always close files (or use 'with open' which auto-closes).")
print("4. 'w' and 'a' create file if not found, 'r' gives error if missing.")
print("5. Use os.path.exists() before deleting to avoid errors.")
print("6. os.rmdir() removes only empty folders.")
print("7. File handling is crucial for web applications and data processing.")

print("\n==============================")
print(" END OF FILE HANDLING DEMO ")
print("==============================")
