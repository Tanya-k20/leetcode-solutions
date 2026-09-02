class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(i) for i in range(1, n + 1)]

        factorial = 1
        for i in range(1, n):
            factorial *= i

        k -= 1  
        ans = []

        while nums:
            index = k // factorial
            ans.append(nums.pop(index))

            if not nums:
                break

            k %= factorial
            factorial //= len(nums)

        return "".join(ans)