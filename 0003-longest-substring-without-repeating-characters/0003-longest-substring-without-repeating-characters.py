class Solution(object):
    def lengthOfLongestSubstring(self, s):
        x = []
        max_len = 0

        for i in s:

            if i in x:
                index = x.index(i)

                for j in range(index + 1):
                    x.pop(0)

            x.append(i)

            if len(x) > max_len:
                max_len = len(x)

        return max_len
        