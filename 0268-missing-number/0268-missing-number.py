class Solution:
    def missingNumber(self, nums):
        nums.sort()

        for i in range(len(nums) + 1):
            if i not in nums:
                return i