#TC: O(n^2) since it is a square matrix
#SC: O(n^2) in this case, but can be optimized to O(1) by directly making the change to the input matrix

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        dp = matrix
        
        for i in range(len(matrix)-2, -1, -1):
            for j in range(len(matrix[0])):
                if j == 0:
                    dp[i][j] = min(matrix[i+1][j], matrix[i+1][j+1]) + matrix[i][j]
                elif j == len(matrix[0]) - 1:
                    dp[i][j] = min(matrix[i+1][j-1], matrix[i+1][j]) + matrix[i][j]
                else:
                    dp[i][j] = min(min(matrix[i+1][j-1], matrix[i+1][j]), matrix[i+1][j+1]) + matrix[i][j]
        
        return min(dp[0])
                
        