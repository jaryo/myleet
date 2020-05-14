class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        re = 0

        for i in range(1, length):
            re += max(0, prices[i] - prices[i-1])
        return re