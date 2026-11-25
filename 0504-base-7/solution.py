class Solution:
    def convertToBase7(self, num: int) -> str:
        import numpy as np
        return np.base_repr(num, base=7)