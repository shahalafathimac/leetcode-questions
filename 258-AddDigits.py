# 258. Add Digits
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
    
        while num>=10:
            store = 0
            for digit in str(num):
                store+=int(digit)
            num = store
        return num



