class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        length = len(s)
        num = 0
        re = 0
        for j in range(k):
            if(s[j] == 'a' or s[j] == 'e' or s[j] == 'i' or s[j] == 'o' or s[j] == 'u'):
                num += 1
        re = num
        
        for j in range(1, length-k+1):
            if(s[j-1] == 'a' or s[j-1] == 'e' or s[j-1] == 'i' or s[j-1] == 'o' or s[j-1] == 'u'):
                num -= 1
            if(s[j+k-1] == 'a' or s[j+k-1] == 'e' or s[j+k-1] == 'i' or s[j+k-1] == 'o' or s[j+k-1] == 'u'):
                num += 1
            re = max(re, num)
            if(re == k):
                break
        
        return re