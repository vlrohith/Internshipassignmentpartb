class BracketValidator:
    def __init__(self):
        self.bracket_map = {')': '(', '}': '{', ']': '['}

    def is_valid(self, input_str):
        stack = []
        for char in input_str:
            if char in self.bracket_map.values():
                stack.append(char)
            elif char in self.bracket_map.keys():
                if not stack or stack.pop() != self.bracket_map[char]:
                    return False
            else:
                # Ignore characters other than brackets
                continue
        return not stack

# Test the BracketValidator class
validator = BracketValidator()

# Test cases
test_str1 = "()"
print(f"Is '{test_str1}' valid? {validator.is_valid(test_str1)}")  # Output: True

test_str2 = "()[]{}"
print(f"Is '{test_str2}' valid? {validator.is_valid(test_str2)}")  # Output: True

test_str3 = "[)"
print(f"Is '{test_str3}' valid? {validator.is_valid(test_str3)}")  # Output: False

test_str4 = "({[)]"
print(f"Is '{test_str4}' valid? {validator.is_valid(test_str4)}")  # Output: False

test_str5 = "{{{"
print(f"Is '{test_str5}' valid? {validator.is_valid(test_str5)}")  # Output: False
