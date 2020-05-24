class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if(not s):
            return True

        temp = []
        
        for i in s:
            if((i >= '0' and i <= '9') or (i >= 'a' and i <= 'z')):
                temp.append(i)
            if(i >= 'A' and i <= 'Z'):
                temp.append(chr(ord(i) + 32))
        
        left = 0
        right = len(temp) - 1

        while(left < right):
            if(temp[left] == temp[right]):
                left += 1
                right -= 1
            else:
                return False
        return True
