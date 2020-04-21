class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        length = len(s)

        con = 0
        num = length
        pos = 1

        while (num > 0):
            if (pos % 2 != 0):
                num -= numRows
                con += 1
            else:
                if(numRows > 1):
                    num -= numRows - 2
                    con += numRows - 2
            pos += 1

        z = [[0 for i in range(con)] for j in range(numRows)]

        pos = 0
        temp = numRows - 2
        pos1 = 0
        nexcon = False

        if(numRows == 1):
            return s

        for j in range(con):
            if(nexcon):
                nexcon = False
            for i in range(numRows):
                if(nexcon):
                    continue
                if(pos == len(s)):
                    break
                if (j % (numRows - 1) == 0):
                    z[i][j] = s[pos]
                    pos += 1
                    temp = numRows - 2
                    pos1 = 0
                else:
                    if (temp > 0):
                        z[i][j] = ' '
                        temp -= 1
                    else:
                        z[i][j] = s[pos]
                        pos += 1
                        pos1 += 1
                        temp = numRows - 2 - pos1
                        nexcon = True
        re = ''

        for i in range(numRows):
            for j in range(con):
                if (z[i][j] == ' ' or z[i][j] == 0):
                    continue
                else:
                    re += z[i][j]

        return re
