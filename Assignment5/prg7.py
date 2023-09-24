import re
def replace_not_poor(string):
    pattern = r"(?<=poor)\snot"
    result = re.sub(pattern, " good", string)
    return result
string = "The lyrics is not that poor!"
result = replace_not_poor(string)
print(result)
string = "The lyrics is poor!"
result = replace_not_poor(string)
print(result)