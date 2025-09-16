"""
Pandas Installation and Basic Usage Demonstration
-------------------------------------------------
This script demonstrates how to install and use Pandas,
create DataFrames, use aliases, and check the version.
"""

# Import required libraries
import pandas  # importing directly without alias
import pandas as pd  # importing with alias (commonly used)
import matplotlib.pyplot as plt

print("="*80)
print("📌 PANDAS INSTALLATION & BASIC USAGE DEMO")
print("="*80)

# ------------------------------------------------------------------------------
# 1. Installation (explained, not executed here)
# ------------------------------------------------------------------------------
print("\n1️⃣ Installation Instructions:")
print("   If Pandas is not installed, use the command:")
print("   👉 pip install pandas")
print("   (If this fails, consider using Anaconda or Spyder, which come with Pandas pre-installed.)")

# ------------------------------------------------------------------------------
# 2. Importing Pandas
# ------------------------------------------------------------------------------
print("\n2️⃣ Importing Pandas:")
print("   - You can import Pandas directly using 'import pandas'")
print("   - OR import with alias 'import pandas as pd' (recommended).")

# ------------------------------------------------------------------------------
# 3. Creating a DataFrame (using pandas without alias)
# ------------------------------------------------------------------------------
print("\n3️⃣ Creating a DataFrame using pandas (without alias):")
mydataset = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3, 7, 2]
}
myvar = pandas.DataFrame(mydataset)
print("\n🔹 DataFrame created:\n")
print(myvar)

# ------------------------------------------------------------------------------
# 4. Creating a DataFrame using pandas alias (pd)
# ------------------------------------------------------------------------------
print("\n4️⃣ Creating a DataFrame using Pandas alias 'pd':")
myvar_alias = pd.DataFrame(mydataset)
print("\n🔹 DataFrame created with alias:\n")
print(myvar_alias)

# ------------------------------------------------------------------------------
# 5. Checking Pandas Version
# ------------------------------------------------------------------------------
print("\n5️⃣ Checking Pandas Version:")
print("🔹 Installed Pandas version is:", pd.__version__)

# ------------------------------------------------------------------------------
# 6. Visualization Example
# ------------------------------------------------------------------------------
print("\n6️⃣ Visualization Example: Cars vs Passings")
print("   👉 Using matplotlib to plot simple bar chart of the DataFrame.")

plt.bar(myvar["cars"], myvar["passings"], color=["skyblue", "salmon", "lightgreen"], edgecolor="black")
plt.title("Number of Passings per Car")
plt.xlabel("Car Brand")
plt.ylabel("Number of Passings")
plt.show()

# ------------------------------------------------------------------------------
# END
# ------------------------------------------------------------------------------
print("\n✅ End of Demonstration. You have now learned:")
print("   - How to install Pandas")
print("   - How to import Pandas (with/without alias)")
print("   - How to create DataFrames")
print("   - How to check Pandas version")
print("   - How to visualize data using matplotlib")
print("="*80)
