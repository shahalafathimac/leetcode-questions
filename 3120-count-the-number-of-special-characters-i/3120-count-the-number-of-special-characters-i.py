class Solution(object):
    def numberOfSpecialChars(self, word):
        lower = set()
        upper = set()

        for ch in word:
            if ch.islower():
                lower.add(ch)
            else:
                upper.add(ch)

        count = 0

        for i in range(26):
            l = chr(ord('a') + i)
            u = chr(ord('A') + i)

            if l in lower and u in upper:
                count += 1

        return count


        