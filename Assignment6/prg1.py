def find_numbers_divisible_by_7_and_multiple_of_5(start_number, end_number):
  result = []
  for number in range(start_number, end_number + 1):
    if number % 7 == 0 and number % 5 == 0:
      result.append(number)
  return result
start_number = 1500
end_number = 2700
result = find_numbers_divisible_by_7_and_multiple_of_5(start_number, end_number)
print(result)
