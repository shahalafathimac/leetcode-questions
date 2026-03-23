class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        start = []
        for p in paths:
            start.append(p[0])
        for p in paths:
            if p[1] not in start:
                return p[1]