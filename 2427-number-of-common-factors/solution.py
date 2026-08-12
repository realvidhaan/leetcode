class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        counter = 0
        for i in range(1, 1001):
            if b%i==0 and a%i==0:
                counter+=1
        return counter