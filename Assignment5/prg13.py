def starts_with_specified_characters(string, specified_characters):
  return string.startswith(specified_characters)
string = "Hello, world!"
specified_characters = "Hello"
result = starts_with_specified_characters(string, specified_characters)
print(result)
string = "Python"
specified_characters = "Py"
result = starts_with_specified_characters(string, specified_characters)
print(result)