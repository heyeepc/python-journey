
nums = [3, 1, 2]

for i in range(len(nums) - 1):
    if nums[i] > nums[i + 1]:
        nums[i], nums[i + 1] = nums[i + 1], nums[i]

print(nums)  # [1, 2, 3]
