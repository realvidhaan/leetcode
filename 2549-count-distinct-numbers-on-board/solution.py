class Solution:
    def distinctIntegers(self, n: int) -> int:
        if n > 2:
            return n-1
        return 1