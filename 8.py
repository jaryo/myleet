class Solution(object):
    def myAtoi(self, str1):
        """
        :type str: str
        :rtype: int
        """
        str1 = str1.strip()

        if(str1 == ''):
            return 0

        if(str1[0] != '-' and str1[0] != '+' and (str1[0] < '0' or str1[0] > '9')):
           return 0

        sign = False

        if (str1[0] == '-'):
            sign = True

        num = 0

        for i in range(len(str1)):

            if ((str1[i] == '+' or str1[i] == '-') and i == 0):
                continue
            if (str1[i] >= '0' and str1[i] <= '9'):
                num = num * 10
                num = num + int(str1[i])
            else:
                break

        if (sign):
            num = -num

        if(num > 2**31-1):
            num = 2**31-1

        if(num < -2**31):
            num = -2**31


        return num