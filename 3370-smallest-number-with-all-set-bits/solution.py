class Solution:
    def smallestNumber(self, n: int) -> int:
        for i in range(n, n**2):
            if bin(i).count('1')==len(bin(i))-2:
                return i
        return 1