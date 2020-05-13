class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if(rowIndex == 0):
            return [1]
        if(rowIndex == 1):
            return [1,1]

        num = [1 for i in range(rowIndex+1)]

        for i in range(2, rowIndex+1):
            for j in range(i+1)[::-1]:
                if(j == 0 or j == i):
                    num[j] = 1
                else:
                    num[j] = num[j] + num[j-1]
                
        return num