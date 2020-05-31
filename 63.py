class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if(obstacleGrid[0][0] == 1):
            return 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0 for i in range(n)] for j in range(m)]

        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if(i == 0 and j == 0):
                    continue
                if(obstacleGrid[i][j] == 1):
                    dp[i][j] = 0
                else:
                    if(i == 0):
                            dp[i][j] = dp[i][j-1]
                    elif(j == 0):
                            dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[-1][-1]