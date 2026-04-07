class Solution(object):
    def countSmaller(self, nums):
        res = [0]*len(nums)
        
        def sort(enum):
            mid = len(enum)//2
            if mid:
                left, right = sort(enum[:mid]), sort(enum[mid:])
                m = len(left)
                i = j = 0
                
                for k in range(len(enum)):
                    if j == len(right) or (i < m and left[i][1] <= right[j][1]):
                        res[left[i][0]] += j
                        enum[k] = left[i]
                        i += 1
                    else:
                        enum[k] = right[j]
                        j += 1
            return enum
        
        sort(list(enumerate(nums)))
        return res