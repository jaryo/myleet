class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        num = 1
        re = '1'
        temp = ''

        for i in range(n):
            if (i > 0):
                re = temp
                temp = ''
                num = 1
            for j in range(len(re)):
                if (j == len(re) - 1):
                    temp += (str(num) + re[j])
                else:
                    if (re[j] == re[j + 1]):
                        num += 1
                    else:
                        temp += (str(num) + re[j])
                        num = 1

        return re