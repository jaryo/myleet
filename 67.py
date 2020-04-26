class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        num = 0

        for i in range(len(a)):
            num += int(a[i])*(2**(len(a)-i-1))

        for i in range(len(b)):
            num += int(b[i])*(2**(len(b)-i-1))

        if (num == 0):
            return '0'

        temp = 0
        re = ''
        while (num >= 2 ** temp):
            temp += 1

        for i in range(temp)[::-1]:
            if (num >= (2**i)):
                num -= (2**i)
                re += '1'
            else:
                re += '0'

        return re