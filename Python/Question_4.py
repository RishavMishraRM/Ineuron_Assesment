def four_sum(nums, target):
    nums.sort()
    n = len(nums)
    quadruplets = set()

    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            left, right = j + 1, n - 1

            while left < right:
                total_sum = nums[i] + nums[j] + nums[left] + nums[right]
                if total_sum == target:
                    quadruplets.add((nums[i], nums[j], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif total_sum < target:
                    left += 1
                else:
                    right -= 1

    return list(quadruplets)

# Example usage:
nums = [1, 0, -1, 0, -2, 2]
target = 0
print(four_sum(nums, target)) 

# Output: [(-2, -1, 1, 2), (-2, 0, 0, 2), (-1, 0, 0, 1)]