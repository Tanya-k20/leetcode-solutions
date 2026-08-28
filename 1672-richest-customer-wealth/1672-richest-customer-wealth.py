class Solution:
    def maximumWealth(self, accounts):
        ans = []

        for account in accounts:
            ans.append(sum(account))

        return max(ans)