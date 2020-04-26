class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if(x == 0):
            return 0

        for i in range(1, 46342):
            if(x/i < i):
                return i-1
            if(x/i == i):
                return i