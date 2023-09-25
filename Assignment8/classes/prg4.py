class TwoSumFinder:
    def find_two_sum(self, numbers, target):
        num_index_map = {}
        for index, num in enumerate(numbers):
            complement = target - num
            if complement in num_index_map:
                return [num_index_map[complement], index]
            num_index_map[num] = index
        return None

# Test the TwoSumFinder class
finder = TwoSumFinder()

# Test case
input_numbers = [90, 20, 10, 40, 50, 60, 70]
target_sum = 50
result = finder.find_two_sum(input_numbers, target_sum)

if result is not None:
    print(f"The pair of elements that sum up to {target_sum} is at indices {result[0]} and {result[1]}.")
else:
    print("No such pair found.")
