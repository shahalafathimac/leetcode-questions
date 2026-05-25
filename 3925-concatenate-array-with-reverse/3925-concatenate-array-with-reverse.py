class Solution(object):
    def concatWithReverse(self, nums):
        ans = []

        for num in nums:
            ans.append(num)

        for i in range(len(nums) - 1, -1, -1):
            ans.append(nums[i])

        return ans
        
        