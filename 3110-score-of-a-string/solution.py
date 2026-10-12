class Solution:
    def scoreOfString(self, s: str) -> int:
        lst  = []
        lst1 = []
        for i in s:
            lst.append(ord(i))
        for j in [(lst[i], lst[i + 1]) for i in range(len(lst) - 1)]:
            lst1.append(abs(j[0]-j[1]))
        return sum(lst1)
        