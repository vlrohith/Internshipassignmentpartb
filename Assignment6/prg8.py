def check_if_square(length, breadth):

  return length == breadth


length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))

if check_if_square(length, breadth):
  print("The rectangle is a square.")
else:
  print("The rectangle is not a square.")
