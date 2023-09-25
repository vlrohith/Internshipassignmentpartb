class StringReverser:
    def reverse_words(self, input_string):
        words = input_string.split()  # Split the input string into words
        reversed_string = ' '.join(reversed(words))  # Reverse the words and join them back
        return reversed_string

# Test the StringReverser class
reverser = StringReverser()

# Test case
input_string = 'hello .py'
result = reverser.reverse_words(input_string)
print(f"Input string: '{input_string}'")
print(f"Reversed string: '{result}'")
