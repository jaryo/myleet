#存一下前缀和，然后从左边开始一个一个拿，计算最大值
class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        length = len(cardPoints)
        dp = range(length + 1)
        re = 0

        for i in range(length):
            dp[i+1] = dp[i] + cardPoints[i]
        
        for i in range(k+1):
            re = max(re, dp[i] + dp[length] - dp[length - k + i])
        
        return re

#维持一个长度为len-k的滑动窗口，取滑动窗口里的值为最小，存一下前缀和
class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        length = len(cardPoints)
        dp = range(length + 1)
        
        for i in range(length):
            dp[i+1] = dp[i] + cardPoints[i]

        re = dp[-1]

        for i in range(k+1):
            num = dp[i + length - k] - dp[i]
            re = min(re, num)

        return dp[-1] - re

#还有一个思路是先全拿左边的，然后右边加左边减，取最大值