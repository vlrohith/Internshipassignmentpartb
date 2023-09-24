sum = 0
product = 1

while True:
  number = input("Enter a number (press q to quit): ")

  if number == "q":
    break

  number = int(number)

  sum += number

  product *= number

average = sum / len(number)

print(f"The average of the numbers is {average}.")
print(f"The product of the numbers is {product}.")
