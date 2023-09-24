def count_elements_greater_than_30(list1):

  count = 0
  for element in list1:
    if element > 30:
      count += 1
  return count


list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

count = count_elements_greater_than_30(list1)

print(f"The number of elements within the list that are greater than 30 is {count}.")
