class ThreeSumFinder:
    def find_three_sum(self, nums):
        nums.sort()  # Sort the input array in ascending order
        triplets = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicates

            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    triplets.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1  # Skip duplicates on the left
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1  # Skip duplicates on the right
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return triplets

# Test the ThreeSumFinder class
finder = ThreeSumFinder()

# Test case
input_numbers = [-25, -10, -7, -3, 2, 4, 8, 10]
result = finder.find_three_sum(input_numbers)

print("Triplets that sum to zero:")
for triplet in result:
    print(triplet)
