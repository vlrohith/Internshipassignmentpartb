class SubsetGenerator:
    def get_unique_subsets(self, nums):
        def backtrack(start, current_subset):
            if start == len(nums):
                subsets.append(current_subset[:])
                return
            # Include the current element in the subset
            current_subset.append(nums[start])
            backtrack(start + 1, current_subset)
            # Exclude the current element from the subset
            current_subset.pop()
            backtrack(start + 1, current_subset)

        subsets = []
        backtrack(0, [])
        return subsets

# Test the SubsetGenerator class
generator = SubsetGenerator()

# Test case
input_nums = [4, 5, 6]
result = generator.get_unique_subsets(input_nums)
print(result)
