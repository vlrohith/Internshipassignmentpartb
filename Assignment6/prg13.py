sum = 0
count = 0

for i in range(10):
  number = int(input("Enter a number: "))

  sum += number

  count += 1

average = sum / count

print(f"The average of the 10 numbers is {average}.")
