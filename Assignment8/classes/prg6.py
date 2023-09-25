class PowerCalculator:
    def my_pow(self, x, n):
        if n == 0:
            return 1
        elif n < 0:
            x = 1 / x
            n = -n
        return self.calculate_power(x, n)

    def calculate_power(self, x, n):
        if n == 0:
            return 1
        half = self.calculate_power(x, n // 2)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x

# Test the PowerCalculator class
calculator = PowerCalculator()

# Test cases
x = 2
n = 10
result = calculator.my_pow(x, n)
print(f"{x}^{n} = {result}")

x = 3
n = -3
result = calculator.my_pow(x, n)
print(f"{x}^{n} = {result}")
