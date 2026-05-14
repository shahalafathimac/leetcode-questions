class Solution(object):

    def isGood(self, nums):

        nums.sort()

        n = nums[-1]

        expected = []

        for i in range(1, n + 1):
            expected.append(i)

        expected.append(n)

        return nums == expected
        