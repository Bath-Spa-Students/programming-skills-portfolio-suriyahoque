# Get the month as input from the user
month = input("Enter the month (e.g., January, February, etc.): ")

# Convert the input to lowercase for case-insensitive comparison
month = month.lower()

# Use the elif statement to determine the season
if month in ["december", "january", "february"]:
    season = "Winter"
elif month in ["march", "april", "may"]:
    season = "Spring"
elif month in ["june", "july", "august"]:
    season = "Summer"
elif month in ["september", "october", "november"]:
    season = "Fall"
else:
    season = "Invalid Month"

# Print the determined season
print("The season for", month.capitalize(), "is", season)