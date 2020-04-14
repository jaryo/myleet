class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if(x < 0):
            return False
        
        s = str(x)
        length = len(s)

        for i in range(length):
            if(s[i] != s[length - i - 1]):
                return False
        
        return True