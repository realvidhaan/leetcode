class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n==1:
            return True
        for i in range(1, 32):
            if 3**i==n:
                return True
        return False