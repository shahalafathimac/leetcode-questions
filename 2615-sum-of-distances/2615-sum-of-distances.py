class Solution(object):
    def distance(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        groups = defaultdict(list)
    
    
        for i, v in enumerate(nums):
            groups[v].append(i)
    
        res = [0] * len(nums)
    
        for g in groups.values():
            prefix = 0
            total = sum(g)
        
            for i, idx in enumerate(g):
                res[idx] = idx * i - prefix + (total - prefix - idx) - idx * (len(g) - i - 1)
                prefix += idx
    
        return res