from scipy import constants
import matplotlib.pyplot as plt

print("============================")
print("      SciPy Constants       ")
print("============================\n")

# ---------------------------------------------------------------
# 1. Basic Constant Example
# ---------------------------------------------------------------
print("[STEP] Example of a scientific constant:")
print("Value of PI:", constants.pi)
print("\n[IMPORTANT NOTE] constants.pi returns the value of mathematical constant π.\n")

# ---------------------------------------------------------------
# 2. Listing All Constants
# ---------------------------------------------------------------
print("[STEP] Listing available constants using dir(constants):")
print(dir(constants))
print("\n[IMPORTANT NOTE] constants module has many categories like metric, mass, time, length, etc.\n")

# ---------------------------------------------------------------
# 3. Metric (SI) Prefixes
# ---------------------------------------------------------------
print("============================")
print("     Metric Prefixes        ")
print("============================")

print("1 kilo =", constants.kilo)
print("1 milli =", constants.milli)
print("1 micro =", constants.micro)
print("1 nano =", constants.nano)

# Visualization of prefixes
metric_prefixes = ["kilo", "milli", "micro", "nano"]
metric_values = [constants.kilo, constants.milli, constants.micro, constants.nano]

plt.figure(figsize=(7,4))
plt.bar(metric_prefixes, metric_values, color="teal")
plt.yscale('log')
plt.title("Metric Prefixes (log scale)")
plt.ylabel("Value")
plt.show()

# ---------------------------------------------------------------
# 4. Binary Prefixes
# ---------------------------------------------------------------
print("\n============================")
print("     Binary Prefixes        ")
print("============================")

print("kibi =", constants.kibi)
print("mebi =", constants.mebi)
print("gibi =", constants.gibi)
print("tebi =", constants.tebi)

# ---------------------------------------------------------------
# 5. Mass Units
# ---------------------------------------------------------------
print("\n============================")
print("     Mass Units             ")
print("============================")

print("1 gram =", constants.gram, "kg")
print("1 pound =", constants.pound, "kg")
print("1 ounce =", constants.ounce, "kg")

# ---------------------------------------------------------------
# 6. Angle Units
# ---------------------------------------------------------------
print("\n============================")
print("     Angle Units            ")
print("============================")

print("1 degree =", constants.degree, "radian")
print("1 arcminute =", constants.arcminute, "radian")
print("1 arcsecond =", constants.arcsecond, "radian")

# ---------------------------------------------------------------
# 7. Time Units
# ---------------------------------------------------------------
print("\n============================")
print("     Time Units             ")
print("============================")

print("1 minute =", constants.minute, "seconds")
print("1 hour =", constants.hour, "seconds")
print("1 day =", constants.day, "seconds")

# ---------------------------------------------------------------
# 8. Length Units
# ---------------------------------------------------------------
print("\n============================")
print("     Length Units           ")
print("============================")

print("1 inch =", constants.inch, "m")
print("1 foot =", constants.foot, "m")
print("1 mile =", constants.mile, "m")
print("1 astronomical unit =", constants.au, "m")
print("1 light year =", constants.light_year, "m")

# ---------------------------------------------------------------
# 9. Pressure Units
# ---------------------------------------------------------------
print("\n============================")
print("     Pressure Units         ")
print("============================")

print("1 atmosphere =", constants.atm, "Pa")
print("1 bar =", constants.bar, "Pa")
print("1 psi =", constants.psi, "Pa")

# ---------------------------------------------------------------
# 10. Area Units
# ---------------------------------------------------------------
print("\n============================")
print("     Area Units             ")
print("============================")

print("1 hectare =", constants.hectare, "m^2")
print("1 acre =", constants.acre, "m^2")

# ---------------------------------------------------------------
# 11. Volume Units
# ---------------------------------------------------------------
print("\n============================")
print("     Volume Units           ")
print("============================")

print("1 liter =", constants.liter, "m^3")
print("1 gallon (US) =", constants.gallon_US, "m^3")

# ---------------------------------------------------------------
# 12. Speed Units
# ---------------------------------------------------------------
print("\n============================")
print("     Speed Units            ")
print("============================")

print("1 km/h =", constants.kmh, "m/s")
print("1 mph =", constants.mph, "m/s")
print("Speed of Sound =", constants.speed_of_sound, "m/s")

# ---------------------------------------------------------------
# 13. Temperature Units
# ---------------------------------------------------------------
print("\n============================")
print("     Temperature Units      ")
print("============================")

print("0 Celsius in Kelvin =", constants.zero_Celsius)
print("1 degree Fahrenheit =", constants.degree_Fahrenheit, "Kelvin")

# ---------------------------------------------------------------
# 14. Energy Units
# ---------------------------------------------------------------
print("\n============================")
print("     Energy Units           ")
print("============================")

print("1 electron volt =", constants.eV, "J")
print("1 calorie =", constants.calorie, "J")
print("1 erg =", constants.erg, "J")

# ---------------------------------------------------------------
# 15. Power Units
# ---------------------------------------------------------------
print("\n============================")
print("     Power Units            ")
print("============================")

print("1 horsepower =", constants.horsepower, "W")

# ---------------------------------------------------------------
# 16. Force Units
# ---------------------------------------------------------------
print("\n============================")
print("     Force Units            ")
print("============================")

print("1 newton (from kgf) =", constants.kilogram_force, "N")
print("1 pound force =", constants.pound_force, "N")

# ---------------------------------------------------------------
print("\n============================")
print("   End of Constants Demo    ")
print("============================")