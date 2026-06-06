class Solution(object):
    def sumOddLengthSubarrays(self, arr):
            n = len(arr)
            ans = 0

            for i in range(n):
                total = (i + 1) * (n - i)
                odd_count = (total + 1) // 2
                ans += arr[i] * odd_count

            return ans
        
        