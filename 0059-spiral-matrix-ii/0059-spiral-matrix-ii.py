class Solution:

    def generateMatrix(self, n: int) -> List[List[int]]:
        
        counter = 1

        top = left = 0

        bottom = right = n - 1

        lst = [[0]*n for _ in range(n)]

        while top <= bottom and left <= right:

            for pos in range(left,right+1):

                lst[top][pos] = counter 

                counter += 1

            top += 1

            for pos in range(top,bottom+1):

                lst[pos][right] = counter

                counter += 1

            right -= 1

            if top <= bottom :

                for pos in range(right,left-1,-1):

                    lst[bottom][pos] = counter

                    counter += 1

                bottom -= 1

            if left <= right :

                for pos in range(bottom,top-1,-1):

                    lst[pos][left] = counter

                    counter += 1

                left += 1

        return lst