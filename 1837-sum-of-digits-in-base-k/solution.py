class Solution:
    def sumBase(self, n: int, k: int) -> int:
        import numpy as np
        lst=[]
        for i in np.base_repr(n, base=k):
            lst.append(int(i))
        return sum(lst)