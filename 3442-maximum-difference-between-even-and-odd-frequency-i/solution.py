class Solution:
    def maxDifference(self, s: str) -> int:
        even = []
        odd = []
        for i in s:
            if s.count(i)%2==0:
                even.append(s.count(i))
            else:
                odd.append(s.count(i))
        return max(odd)-min(even)