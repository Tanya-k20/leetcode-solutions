from collections import Counter

class Solution:
    def findShortestSubArray(self, nums):
        count = Counter(nums)

        degree = max(count.values())
        ans = len(nums)

        first = {}
        last = {}

        for i, num in enumerate(nums):
            if num not in first:
                first[num] = i
            last[num] = i

        for num in count:
            if count[num] == degree:
                ans = min(ans, last[num] - first[num] + 1)

        return ans