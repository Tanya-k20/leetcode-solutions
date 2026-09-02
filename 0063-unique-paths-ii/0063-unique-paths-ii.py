class Solution:

    def uniquePathsWithObstacles(self, obstacleGrid):

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[-1] * n for _ in range(m)]

        def solve(i, j):

            # Outside the grid
            if i < 0 or j < 0:
                return 0

            # Obstacle
            if obstacleGrid[i][j] == 1:
                return 0

            # Starting cell
            if i == 0 and j == 0:
                return 1

            # Already calculated
            if dp[i][j] != -1:
                return dp[i][j]

            up = solve(i - 1, j)
            left = solve(i, j - 1)

            dp[i][j] = up + left

            return dp[i][j]

        return solve(m - 1, n - 1)