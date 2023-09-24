def string_both_ends(string):
    if len(string) < 2:
        return ""
    else:
        return string[:2] + string[-2:]
string = "thisisniceone"
result = string_both_ends(string)
print(result)
string = "ab"
result = string_both_ends(string)
print(result)
string = "f"
result = string_both_ends(string)
print(result)