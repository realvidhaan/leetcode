class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        lst = []
        for i in s:
            if i in t:
                lst.append(abs(s.index(i)-t.index(i)))
        return sum(lst)