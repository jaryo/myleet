class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        st = s[::-1]
        length = len(st)

        for i in range(length):
            if(st[i] == 'I'):
                if(i > 0 and (st[i-1] == 'V' or st[i-1] == 'X')):
                    continue
                num += 1
            
            if(st[i] == 'V'):
                if(i+1 <= length-1 and st[i+1] == 'I'):
                    num -= 1
                num += 5
            
            if(st[i] == 'X'):
                if(i+1 <= length-1 and st[i+1] == 'I'):
                    num -= 1
                if(i > 0 and (st[i-1] == 'L' or st[i-1] == 'C')):
                    continue
                num += 10

            if(st[i] == 'L'):
                if(i+1 <= length-1 and st[i+1] == 'X'):
                    num -= 10
                num += 50
            
            if(st[i] == 'C'):
                if(i+1 <= length-1 and st[i+1] == 'X'):
                    num -= 10
                if(i > 0 and (st[i-1] == 'D' or st[i-1] == 'M')):
                    continue
                num += 100
            
            if(st[i] == 'D'):
                if(i+1 <= length-1 and st[i+1] == 'C'):
                    num -= 100
                num += 500

            if(st[i] == 'M'):
                if(i+1 <= length-1 and st[i+1] == 'C'):
                    num -= 100
                num += 1000
        
        return num