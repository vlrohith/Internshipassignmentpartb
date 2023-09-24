# Create three empty lists
even_numbers = []
odd_numbers = []
prime_numbers = []

# Iterate over the range(1,101)
for number in range(1,101):
  # Check if the number is even
  if number % 2 == 0:
    # Add the number to the even_numbers list
    even_numbers.append(number)
  # Otherwise, the number is odd
  else:
    # Add the number to the odd_numbers list
    odd_numbers.append(number)

  # Check if the number is prime
  if number > 1:
    for i in range(2, int(number**0.5) + 1):
      if number % i == 0:
        break
    else:
      # Add the number to the prime_numbers list
      prime_numbers.append(number)

# Print the three lists
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
print("Prime numbers:", prime_numbers)
