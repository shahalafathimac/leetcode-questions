class Solution(object):
   def majorityElement(self,nums):
    count = {}

    for num in nums:
        count[num] = count.get(num, 0) + 1

        if count[num] > len(nums) // 2:
            return num


    nums = [2,2,1,1,1,2,2]
    print(majorityElement(nums))  
        