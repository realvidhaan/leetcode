class Solution:
    def reverse(self, x: int) -> int:
        reverse = str(abs(x))
        bob=int(reverse[::-1])
        if bob > 2**31 - 1:  
            return 0  
        if x>0:
            return bob
        return -bob