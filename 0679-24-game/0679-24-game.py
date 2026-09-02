from math import isclose
class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
      TARGET = 24.0
      EPS = 1e-4
      nums = [float(x) for x in cards]
      def dfs(a: list[float]) -> bool:
          n = len(a)
          if n == 1:
              return abs(a[0] - TARGET) < EPS
          for i in range(n):
              for j in range(i + 1, n):
                  x, y = a[i], a[j]
                  rest = [a[k] for k in range(n) if k != i and k != j]
                  for v in (x + y, x * y, x - y, y - x):
                      if dfs(rest + [v]):
                          return True
                  if abs(y) > EPS and dfs(rest + [x / y]):
                      return True
                  if abs(x) > EPS and dfs(rest + [y / x]):
                      return True
          return False
      return dfs(nums)