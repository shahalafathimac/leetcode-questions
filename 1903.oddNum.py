# 1903. Largest Odd Number in String
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given a string num, representing a large integer. Return the largest-valued odd integer (as a string) that is a non-empty substring of num, or an empty string "" if no odd integer exists.

# A substring is a contiguous sequence of characters within a string.

 

# Example 1:

# Input: num = "52"
# Output: "5"
# Explanation: The only non-empty substrings are "5", "2", and "52". "5" is the only odd number


class Solution(object):
    def largestOddNumber(self, nums):
        """
        :type num: str
        :rtype: str
        """
        
        for i in range(len(nums) - 1, -1, -1):
            if int(nums[i]) % 2 != 0:
                return nums[:i+1]
        return ""
            