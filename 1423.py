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
            dp[i+1] = dp[i] + cardPoints[i]#前缀和

        re = dp[-1]

        for i in range(k+1):#拿k个求最大，只需维持一个length-k长度的滑动区间，区间和最小即可
            num = dp[i + length - k] - dp[i]
            re = min(re, num)

        return dp[-1] - re