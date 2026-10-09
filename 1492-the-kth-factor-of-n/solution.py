class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        lst = []
        for i in range(1, n+1):
            if n%i==0:
                lst.append(i)
        return lst[k - 1] if 1 <= k <= len(lst) else -1