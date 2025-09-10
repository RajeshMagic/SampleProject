# ===============================================================
# PYTHON PIP (Package Installer for Python) - DEMONSTRATION
# ===============================================================
# PIP = Python's package manager
# - Used to install, upgrade, remove, and list Python packages.
# - By default included from Python 3.4+
#
# A package = a collection of modules (Python code libraries).
# ===============================================================

import sys
import subprocess

print("\n==============================")
print(" 1. CHECKING PIP VERSION ")
print("==============================")

# Checking pip version using subprocess
try:
    result = subprocess.run(["pip", "--version"], capture_output=True, text=True)
    print("PIP version info:", result.stdout.strip())
    print("Important Note: If you see version details, pip is installed.\n")
except Exception as e:
    print("PIP not installed. You can download from https://pypi.org/project/pip/\n")


print("==============================")
print(" 2. INSTALLING A PACKAGE (Example: camelcase) ")
print("==============================")
print("Command to run in terminal:")
print("   pip install camelcase")
print("Important Note: Run above command in terminal, not inside Python script.\n")


print("==============================")
print(" 3. USING AN INSTALLED PACKAGE ")
print("==============================")

try:
    import camelcase

    c = camelcase.CamelCase()
    txt = "hello world, welcome to python pip demo"
    print("Original text:", txt)
    print("After applying camelcase:", c.hump(txt))
    print("Important Note: camelcase.CamelCase().hump() converts words into CamelCase style.\n")

except ImportError:
    print("Camelcase package not installed. Please install it using:")
    print("   pip install camelcase\n")


print("==============================")
print(" 4. UNINSTALLING A PACKAGE ")
print("==============================")
print("Command to run in terminal:")
print("   pip uninstall camelcase")
print("Important Note: PIP will ask for confirmation (y/n) before uninstalling.\n")


print("==============================")
print(" 5. LISTING INSTALLED PACKAGES ")
print("==============================")

try:
    result = subprocess.run(["pip", "list"], capture_output=True, text=True)
    print("Installed packages:\n", result.stdout.strip())
    print("Important Note: pip list shows all installed packages and versions.\n")
except Exception as e:
    print("Could not list packages. Ensure pip is available.\n")


print("==============================")
print(" END OF PIP DEMO ")
print("==============================\n")
