class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        a = set(sentence)
        c = len(a)
        if c == 26 :
            return True
        else:
            return False