class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
    
        while num>=10:
            store = 0
            for digit in str(num):
                store+=int(digit)
            num = store
        return num

       
