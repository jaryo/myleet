class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        a = []
        num = 0
        f = False

        if(x < 0):
            f = True
            x = abs(x)

        while x > 0:
            a.append(x % 10)
            x = x / 10
        
        for i in a:
            num = num * 10
            num = num + i
        
        if(f):
            num = -num

        if(num > 2147483647 or num < -2147483648):
            num = 0

        return num