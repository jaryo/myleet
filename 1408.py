class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        length = len(words)
        re = set([])

        for i in range(length):
            for j in range(length):
                if(i == j):
                    continue
                
                if(words[i] in words[j]):
                    re.add(words[i])
        
        re = list(re)
        
        return re