class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        length = len(s)
        rec = []

        for i in range(length):
            if(s[i] == ' '):
                rec.append(i)
            
        if(s == '' or len(rec) == length):
            return 0
        elif(len(rec) == 0):
            return length
        else:
            return length - 1 - rec[-1]