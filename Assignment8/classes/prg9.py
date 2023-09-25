class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2  # Pi * r^2 for area

    def perimeter(self):
        return 2 * 3.14159 * self.radius  # 2 * Pi * r for perimeter

# Create an instance of the Circle class with a radius of 5
circle = Circle(5)

# Calculate and print the area and perimeter
print("Area:", circle.area())
print("Perimeter:", circle.perimeter())
