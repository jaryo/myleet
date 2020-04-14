class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st = []

        for i in range(len(s)):
            if(s[i] == ' '):
                continue
            if(s[i] == '('):
                st.append(')')
            if(s[i] == '['):
                st.append(']')
            if(s[i] == '{'):
                st.append('}')
            if(s[i] == ')' or s[i] == ']' or s[i] == '}'):
                if(len(st) == 0):
                    return False
                else:
                    if(s[i] != st.pop()):
                        return False
        
        if(len(st) > 0):
            return False
        
        return True