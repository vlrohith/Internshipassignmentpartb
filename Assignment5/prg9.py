def remove_nth_char(string, n):
    if n < 0 or n >= len(string):
        raise ValueError("n must be a valid index in the string.")
    return string[:n] + string[n + 1:]
string = "Hello, world!"
n = 5
result = remove_nth_char(string, n)
print(result)