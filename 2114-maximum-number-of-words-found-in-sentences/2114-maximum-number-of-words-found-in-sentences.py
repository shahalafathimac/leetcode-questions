class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        count = 0
        for i in sentences:
            a = i.split(" ")
            b= len(a)
            if b>count:
                count = b
        return count
            
            
