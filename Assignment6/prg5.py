def calculate_sum_and_average(numbers):

  sum = 0
  for number in numbers:
    sum += number
  average = sum / len(numbers)
  return sum, average


numbers = []
while True:
  number = int(input("Enter a number (0 to finish): "))
  if number == 0:
    break
  numbers.append(number)

sum, average = calculate_sum_and_average(numbers)

print(f"The sum of the numbers is {sum}.")
print(f"The average of the numbers is {average}.")
