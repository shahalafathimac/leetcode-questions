class Solution(object):
    def triangleType(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        
        nums.sort()
        a,b,c = nums
        if a + b <= c:
            return 'none'

        if a == b == c :
            return "equilateral"
        elif a == b or b == c or c == a :
            return "isosceles"
        else:
            return "scalene"