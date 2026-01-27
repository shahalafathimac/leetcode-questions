
Code
Testcase
Testcase
Test Result
2535. Difference Between Element Sum and Digit Sum of an Array
Solved
Easy
Topics
premium lock icon
Companies
Hint
You are given a positive integer array nums.

The element sum is the sum of all the elements in nums.
The digit sum is the sum of all the digits (not necessarily distinct) that appear in nums.
Return the absolute difference between the element sum and digit sum of nums.

Note that the absolute difference between two integers x and y is defined as |x - y|.



class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        DigitSum=0
        for num in nums:
            total+=num
        for num in nums:
            for digit in str(num):
                DigitSum+= int(digit)
        return abs (total-DigitSum)