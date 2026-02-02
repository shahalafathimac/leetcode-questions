# 2520. Count the Digits That Divide a Number
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an integer num, return the number of digits in num that divide num.

# An integer val divides nums if nums % val == 0.


class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        count = 0
        a = str(num)
        for i in a:
            if num % int(i)==0:
                count+=1
        return count