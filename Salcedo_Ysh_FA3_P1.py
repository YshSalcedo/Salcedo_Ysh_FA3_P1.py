# Get the user's input for points to add
user_input = input("How many points? ")

# Check if the input is blank 
# We need to validate before converting to integer
if user_input == "":
    print("You did not enter anything. Please enter a whole number.")
    # Stop the program execution
    exit()

# Check if the input consists only of digits 
# Using isdigit() ensures the string contains only numeric characters
if not user_input.isdigit():
    print("That is not a whole number. Please enter digits only.")
    exit()

# Convert the validated input to an integer for calculation
points = int(user_input)

# Selection structure to determine bonus based on points
# We use 3 branches: points < 100, points == 100, points > 100
# This covers all possible cases with the given rules
if points < 100:
    bonus = 0
elif points == 100:
    bonus = 5
else:  # points > 100
    bonus = 10

# Calculate the new total by adding bonus to points
new_total = points + bonus

# Print the results with clear labels for each value
print("Points added:", points)
print("Bonus given:", bonus)
print("New total:", new_total)