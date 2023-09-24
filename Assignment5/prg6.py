def add_suffix(string):
    if len(string) < 3:
        return string
    elif string[-3:] == "ing":
        return string + "ly"
    else:
        return string + "ing"
string = "abc"
result = add_suffix(string)
print(result)
string = "string"
result = add_suffix(string)
print(result)