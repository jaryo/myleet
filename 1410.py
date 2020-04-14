class Solution(object):
    def entityParser(self, text):
        """
        :type text: str
        :rtype: str
        """
        length = len(text)
        html = ["&quot;", "&apos;", "&amp;", "&gt;", "&lt;", "&frasl;"]
        ch = ['\"', '\'', '&', '>', '<', '/']

        search = ""
        has = False
        pos = -1

        re = ""

        for i in range(length):
            if(i <= pos):
                continue
            if (text[i] == '&'):
                pos = i
                while (text[pos] != ';'):
                    search = search + text[pos]
                    pos = pos + 1

                search = search + ';'

                for j in range(len(html)):
                    if (search == html[j]):
                        re = re + ch[j]
                        has = True
                        break

                if(not has):
                    pos = 0
                    re = re + '&'

                search = ""
                has = False
                continue

            re = re + text[i]

        return re