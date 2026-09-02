class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        ans = []
        visited = [False] * len(nums)

        def backtrack(curr):
            if len(curr) == len(nums):
                ans.append(curr[:])
                return

            for i in range(len(nums)):
                if visited[i]:
                    continue

                if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                    continue

                visited[i] = True
                curr.append(nums[i])

                backtrack(curr)

                curr.pop()
                visited[i] = False

        backtrack([])
        return ans