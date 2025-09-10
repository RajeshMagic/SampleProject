# ===============================================================
# PYTHON DATETIME - DEMONSTRATION
# ===============================================================
# The datetime module in Python helps us work with dates and times.
# A "date" in Python is not a native data type, but datetime gives
# us a DateTime class to handle and manipulate date/time objects.
# ===============================================================

import datetime

print("\n==============================")
print(" 1. GETTING CURRENT DATE & TIME ")
print("==============================")

# Get the current local date and time
now = datetime.datetime.now()
print("Current Date & Time:", now)
print("Important Note: datetime.now() returns year, month, day, hour, "
      "minute, second, microsecond all together.")


print("\n==============================")
print(" 2. ACCESSING YEAR, WEEKDAY NAME ")
print("==============================")

print("Year:", now.year)
print("Weekday (Full Name):", now.strftime("%A"))
print("Important Note: strftime('%A') gives the full weekday name, "
      "like Monday, Tuesday, etc.")


print("\n==============================")
print(" 3. CREATING CUSTOM DATE OBJECTS ")
print("==============================")

# Create a date object for May 17, 2020
custom_date = datetime.datetime(2020, 5, 17)
print("Custom Date (2020, 5, 17):", custom_date)
print("Important Note: datetime(year, month, day) is mandatory. "
      "Hour, minute, second are optional and default to 0.")


print("\n==============================")
print(" 4. FORMATTING DATES WITH strftime() ")
print("==============================")

# Example date
example_date = datetime.datetime(2018, 6, 1)

print("Date:", example_date)

# Formatting examples
print("Month (Full):", example_date.strftime("%B"))   # June
print("Month (Short):", example_date.strftime("%b"))  # Jun
print("Day of Month:", example_date.strftime("%d"))   # 01
print("Year (Full):", example_date.strftime("%Y"))    # 2018
print("Year (Short):", example_date.strftime("%y"))   # 18
print("Weekday (Short):", example_date.strftime("%a")) # Fri
print("Weekday (Number, Sun=0):", example_date.strftime("%w")) # 5
print("Important Note: strftime() is used to convert a datetime object "
      "into a formatted string representation.")


print("\n==============================")
print(" 5. TIME FORMATTING EXAMPLES ")
print("==============================")

print("Hour (24-hour):", now.strftime("%H"))
print("Hour (12-hour):", now.strftime("%I"))
print("AM/PM:", now.strftime("%p"))
print("Minute:", now.strftime("%M"))
print("Second:", now.strftime("%S"))
print("Microsecond:", now.strftime("%f"))


print("\n==============================")
print(" 6. DATE & TIME VARIANTS ")
print("==============================")

print("Local Version of Date & Time (%c):", now.strftime("%c"))
print("Local Date (%x):", now.strftime("%x"))
print("Local Time (%X):", now.strftime("%X"))
print("Day of Year (%j):", now.strftime("%j"))
print("Week Number (Sunday First, %U):", now.strftime("%U"))
print("Week Number (Monday First, %W):", now.strftime("%W"))
print("ISO Year (%G):", now.strftime("%G"))
print("ISO Weekday (%u):", now.strftime("%u"))
print("ISO Week Number (%V):", now.strftime("%V"))


print("\n==============================")
print(" 7. SPECIAL FORMATTING NOTES ")
print("==============================")

print("Century (%C):", now.strftime("%C"))
print("Literal Percent Sign (%%):", now.strftime("100%% Sure"))
print("Important Note: %% is used to print the % symbol literally "
      "when using strftime().")


print("\n==============================")
print(" END OF PYTHON DATETIME DEMO ")
print("==============================\n")
