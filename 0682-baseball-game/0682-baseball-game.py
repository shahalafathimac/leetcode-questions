class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        store = []

        for n in operations:
            if n == "C":
                store.pop()

            elif n == "D":
                store.append(store[-1] * 2)

            elif n == "+":
                store.append(store[-1]+store[-2])

            else:
                store.append(int(n))

        return sum(store)

