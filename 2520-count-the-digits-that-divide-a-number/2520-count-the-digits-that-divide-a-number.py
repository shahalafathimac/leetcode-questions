class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        count = 0
        a = str(num)
        for i in a:
            if num % int(i)==0:
                count+=1
        return count
            
        
