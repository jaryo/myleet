class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if(strs == []):
            return ""

        num = len(strs[0])
        for s in strs:
            length = len(s)
            if(length < num):
                num = length
            
        test = set()
        addone = ''
        final = ''

        for i in range(num):
            for s in strs:
                test.add(s[i])
                addone = s[i]
            
            if(len(test) > 1):
                break
            
            test.remove(addone)
            final += addone
        
        return final