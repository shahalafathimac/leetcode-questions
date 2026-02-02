
# Code


# Testcase
# Testcase
# Test Result
# 2108. Find First Palindromic String in the Array
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".

# A string is palindromic if it reads the same forward and backward.



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
           
           



            

