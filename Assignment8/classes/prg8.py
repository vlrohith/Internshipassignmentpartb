class StringManipulator:
    def __init__(self):
        self.input_string = ""

    def get_string(self):
        self.input_string = input("Enter a string: ")

    def print_string(self):
        reversed_string = self.input_string[::-1]
        print("Reversed string:", reversed_string)

# Create an instance of the StringManipulator class
manipulator = StringManipulator()

# Get a string from the user
manipulator.get_string()

# Print the reversed string
manipulator.print_string()
