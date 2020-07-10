import sys

class Solution(object):
    def minScoreTriangulation(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # return self.recursion(A, 0, len(A)-1)
        return self.dynamic(A)

    def recursion(self, A, start, end):
        if (start+2) == end:
            return A[start] * A[start+1] * A[end]

        firstSum = A[start] * A[start+1] * A[end] + self.recursion(A, start+1, end)
        lastSum = A[start] * A[end] * A[end-1] + self.recursion(A, start, end-1)
        minSum = min(firstSum, lastSum)

        for k in range(start+2, end-1):
            curSum = self.recursion(A, start, k) + self.recursion(A, k, end) + A[start] * A[k] * A[end]
            minSum = min(minSum, curSum)
            
        return minSum

    def dynamic(self, A):
        length = len(A)
        productMap = [[0 for i in range(length)] for j in range(length)]
        for size in range(3, length+1):
            for i in range(length - size + 1):
                if size == 3:
                    productMap[i][i+2] = A[i] * A[i+1] * A[i+2]
                else:
                    minSum = sys.maxsize
                    j = i + size - 1
                    for k in range(i+1, j):
                        curSum = productMap[i][k] + A[i] * A[k] * A[j] + productMap[k][j]
                        minSum = min(minSum, curSum)
                    productMap[i][j] = minSum
        
        return productMap[0][length-1]
                    

solution = Solution()
solution.minScoreTriangulation([1,3,1,4,1,5])