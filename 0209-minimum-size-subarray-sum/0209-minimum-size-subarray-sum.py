class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        sum_i = 0
        min_len = float('inf')
        while right < len(nums):
            sum_i+=nums[right]
            while sum_i >= target:
                min_len = min(min_len,right-left+1)
                sum_i-=nums[left]
                left+=1
            right+=1

        return min_len if min_len!=float('inf') else 0