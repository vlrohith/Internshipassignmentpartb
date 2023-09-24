def check_triangle_type(x, y, z):

  if x == y == z:
    return "equilateral"
  elif x == y or y == z or z == x:
    return "isosceles"
  else:
    return "scalene"

x = 6
y = 8
z = 12

triangle_type = check_triangle_type(x, y, z)

print(f"The triangle is a {triangle_type} triangle.")
