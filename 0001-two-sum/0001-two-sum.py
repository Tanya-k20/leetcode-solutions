class Solution:
    def twoSum(self, nums, target):
        dic={}
        for i in range(len(nums)):
            c=target-nums[i]
            if c in dic:
                return [dic[c],i]
            dic[nums[i]]=i    