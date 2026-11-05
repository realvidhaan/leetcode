class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        lst =[]
        for i, j in enumerate(nums):
            if bin(i).count('1') == k:
                lst.append(j)
        return sum(lst)