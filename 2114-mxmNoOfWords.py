# 2114. Maximum Number of Words Found in Sentences
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# A sentence is a list of words that are separated by a single space with no leading or trailing spaces.

# You are given an array of strings sentences, where each sentences[i] represents a single sentence.

# Return the maximum number of words that appear in a single sentence.


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
            
            
