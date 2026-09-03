class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        matchsticks.sort(reverse=True)
        n = len(matchsticks)
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        side = total // 4

        def dp(used, curr, memo: dict):
            if curr > side:
                return False
            if curr == side:
                return dp(used, 0, memo)
            if used == (1 << n) - 1:
                return curr == 0

            if (used, curr) not in memo:
                for i in range(n):
                    if not (used & (1 << i)):
                        if dp(used | (1 << i), curr + matchsticks[i], memo):
                            memo[(used, curr)] = True
                            return True
            memo[(used, curr)] = False
            return memo[(used, curr)]
        return dp(0, 0, {})