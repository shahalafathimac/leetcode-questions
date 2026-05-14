class Solution(object):
    def recoverOrder(self, order, friends):
        result = []
        for i in order:
            if i in friends:
                result.append(i)
        return result

        