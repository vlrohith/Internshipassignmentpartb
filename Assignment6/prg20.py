def square_list(list1):


  squared_list = []
  for number in list1:
    squared_list.append(number * number)
  return squared_list

list1 = [1, 2, 3, 4, 5]
squared_list = square_list(list1)

print("Squared list:", squared_list)
