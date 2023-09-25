class RomanConverter:
    def __init__(self):
        self.roman_numerals = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }

    def int_to_roman(self, num):
        result = ''
        for value in sorted(self.roman_numerals.keys(), reverse=True):
            while num >= value:
                result += self.roman_numerals[value]
                num -= value
        return result

    def roman_to_int(self, roman):
        result = 0
        i = 0
        while i < len(roman):
            if i + 1 < len(roman) and roman[i:i + 2] in self.roman_numerals.values():
                result += list(self.roman_numerals.keys())[list(self.roman_numerals.values()).index(roman[i:i + 2])]
                i += 2
            else:
                result += list(self.roman_numerals.keys())[list(self.roman_numerals.values()).index(roman[i])]
                i += 1
        return result

# Test the RomanConverter class
converter = RomanConverter()

# Convert integer to Roman numeral
integer_value = 1987
roman_numeral = converter.int_to_roman(integer_value)
print(f"{integer_value} in Roman numerals is: {roman_numeral}")

# Convert Roman numeral to integer
roman_value = "MMXIX"
integer_numeral = converter.roman_to_int(roman_value)
print(f"{roman_value} in integer form is: {integer_numeral}")
