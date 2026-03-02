class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        store = []
    
        for n in nums:
            if n in store:
                store.remove(n)
            else:
                store.append(n)
        return store[0]
