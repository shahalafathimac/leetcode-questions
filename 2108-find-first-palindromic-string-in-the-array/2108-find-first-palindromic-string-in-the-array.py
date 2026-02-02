class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        ary = []
        for i in words:
            if i == i[::-1]:
                ary.append(i)
                break
        if len(ary)== 0:
             return ""
        else:
            return ary[0]
           
           



            

