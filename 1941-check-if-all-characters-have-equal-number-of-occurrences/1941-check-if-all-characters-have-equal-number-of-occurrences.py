class Solution(object):
    def areOccurrencesEqual(self, s):
        for n in s:
            if s.count(n)!= s.count(s[0]):
                return False
        return True