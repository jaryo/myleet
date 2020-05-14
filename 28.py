class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if(needle == ''):
            return 0

        length = len(haystack)
        rec = []

        for i in range(length):
            if(needle[0] == haystack[i]):
                left = i
                right = i + len(needle) - 1
                if(right > length - 1):
                    break
                else:
                    pos = len(needle) - 1
                    while(left < right):
                        if(haystack[right] == needle[pos]):
                            right -= 1
                            pos -= 1
                        else:
                            break
                    if(left == right):
                        return left
        
        return -1