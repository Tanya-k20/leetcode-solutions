class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        ans, cur = [], []
        def bt(i):
            ans.append(cur[:])
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j-1]: continue
                cur.append(nums[j])
                bt(j + 1)
                cur.pop()
        bt(0)
        return ans