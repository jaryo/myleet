class Solution(object):
    def processQueries(self, queries, m):
        """
        :type queries: List[int]
        :type m: int
        :rtype: List[int]
        """

        P = range(1, m+1)
        length = len(P)
        re = []

        for i in queries:
            for j in range(length):
                if(i == P[j]):
                    re.append(j)

                    P.remove(0)
                    P.insert(0, temp)
                    break
        
        return re