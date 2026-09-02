class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)

        isPalin = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            isPalin[i][i] = True

            for j in range(i + 1, n):
                if s[i] == s[j]:
                    if isPalin[i + 1][j - 1] or j - i < 2:
                        isPalin[i][j] = True

        dp = [float("inf")] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            for j in range(i):
                if isPalin[j][i - 1]:
                    dp[i] = min(dp[i], dp[j] + 1)

        return dp[n] - 1