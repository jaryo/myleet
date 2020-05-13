class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if(numRows == 0):
            return []
        if(numRows == 1):
            return [[1]]
        if(numRows == 2):
            return [[1], [1,1]]

        re = []
        re.append([1])
        re.append([1,1])

        for i in range(2, numRows):
            temp = []
            for j in range(i+1):
                if(j == 0 or j == i):
                    temp.append(1)
                    continue
                else:
                    temp.append(re[i-1][j-1] + re[i-1][j])
            re.append(temp)
        
        return re