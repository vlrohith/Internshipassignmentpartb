# Create an empty list
list1 = []

# Take inputs from the user to make the list
while True:
  # Prompt the user to enter a number
  number = input("Enter a number (press q to quit): ")

  # If the user presses q, break out of the loop
  if number == "q":
    break

  # Add the number to the list
  list1.append(number)

# Take one input from the user to search in the list
number_to_search = input("Enter a number to search for: ")

# Check if the number to search is in the list
if number_to_search in list1:
  # Remove the number from the list
  list1.remove(number_to_search)

  # Print a message to the user
  print(f"The number {number_to_search} has been removed from the list.")
else:
  # Print a message to the user
  print(f"The number {number_to_search} is not in the list.")

# Iterate over the list using a for loop
for number in list1:
  # Print the number to the console
  print(number)
