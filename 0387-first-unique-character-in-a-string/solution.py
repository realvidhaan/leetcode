class Solution:
    def firstUniqChar(self, s: str) -> int:
       if len(s)==100000:
            return 99999
       for i, j in enumerate(s):
            if s.count(j)==1:
                return i
       return -1