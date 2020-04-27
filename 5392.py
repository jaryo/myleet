class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        num = 0
        for i in range(1, length):
            if(s[i] == '1'):
                num += 1
        
        if(s[0] == '0'):
            num += 1
        temp = num

        for i in range(1, length - 1):
            if(s[i] == '0'):
                temp += 1
            if(s[i] == '1'):
                temp -= 1
            num = max(num, temp)
        
        return num