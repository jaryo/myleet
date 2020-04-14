class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        set1 = ['I','II','III','VI','V','IV','IIV','IIIV','XI']
        set2 = ['X','XX','XXX','LX','L','XL','XXL','XXXL','CX']
        set3 = ['C','CC','CCC','DC','D','CD','CCD','CCCD','MC']
        set4 = ['M','MM','MMM']

        set5 = [set1,set2,set3,set4]

        s = str(num)[::-1]
        s1 = ''

        for i in range(len(s)):
            if(int(s[i]) == 0):
                continue
            s1 += set5[i][int(s[i])-1]
        
        s1 = s1[::-1]

        return s1