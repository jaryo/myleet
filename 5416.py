class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        length = len(sentence)
        
        temp = ''
        words = []
        
        for i in range(length):
            if(sentence[i] != ' '):
                temp += sentence[i]
            if(sentence[i] == ' ' or i == length - 1):
                words.append(temp)
                temp = ''
        
        for i in range(len(words)):
            if(searchWord[0] == words[i][0] and searchWord in words[i]):
                return i+1
        return -1