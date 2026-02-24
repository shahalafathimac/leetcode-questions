class Solution(object):
    def addDigits(self, nums):
        """
        :type num: int
        :rtype: int
        """
    
        while nums>=10:
            store = 0
            for digit in str(nums):
                store+=int(digit)
            nums = store
        return nums

       
