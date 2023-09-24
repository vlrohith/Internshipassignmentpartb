# Create two empty lists
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Create new lists for each divisor
divisible_by_4 = []
divisible_by_6 = []
divisible_by_8 = []
divisible_by_10 = []
divisible_by_3 = []
divisible_by_5 = []
divisible_by_7 = []
divisible_by_9 = []

# Iterate over the two lists and add the numbers to the corresponding new lists
for number in list_1:
  if number % 4 == 0:
    divisible_by_4.append(number)
  if number % 6 == 0:
    divisible_by_6.append(number)
  if number % 8 == 0:
    divisible_by_8.append(number)
  if number % 10 == 0:
    divisible_by_10.append(number)
  if number % 3 == 0:
    divisible_by_3.append(number)
  if number % 5 == 0:
    divisible_by_5.append(number)
  if number % 7 == 0:
    divisible_by_7.append(number)
  if number % 9 == 0:
    divisible_by_9.append(number)

for number in list_2:
  if number % 4 == 0:
    divisible_by_4.append(number)
  if number % 6 == 0:
    divisible_by_6.append(number)
  if number % 8 == 0:
    divisible_by_8.append(number)
  if number % 10 == 0:
    divisible_by_10.append(number)
  if number % 3 == 0:
    divisible_by_3.append(number)
  if number % 5 == 0:
    divisible_by_5.append(number)
  if number % 7 == 0:
    divisible_by_7.append(number)
  if number % 9 == 0:
    divisible_by_9.append(number)

# Print the new lists
print("Divisible by 4:", divisible_by_4)
print("Divisible by 6:", divisible_by_6)
print("Divisible by 8:", divisible_by_8)
print("Divisible by 10:", divisible_by_10)
print("Divisible by 3:", divisible_by_3)
print("Divisible by 5:", divisible_by_5)
print("Divisible by 7:", divisible_by_7)
print("Divisible by 9:", divisible_by_9)
