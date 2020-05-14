class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        length = len(digits)
        num = 0
        re = []

        for i in range(length):
            num *= 10
            num += digits[i]
        
        num += 1
        while(num > 0):
            re.append(num % 10)
            num /= 10
        
        return re[::-1]