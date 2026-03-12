class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        richest = 0
        for n in accounts:
            wealth = sum(n)
            richest = max(richest,wealth)
        return richest