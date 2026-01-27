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
