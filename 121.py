class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if(not prices):
            return 0

        length = len(prices)
        dp = [0 for x in range(length)]
        minp = prices[0]

        for i in range(1, length):
            dp[i] = max(dp[i-1], prices[i] - minp)
            if(prices[i] < minp):
             minp = prices[i]
            
        return dp[-1]