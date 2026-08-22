class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        lst = []
        for i in str(n):
            lst.append(int(i))
        return math.prod(lst)-sum(lst)