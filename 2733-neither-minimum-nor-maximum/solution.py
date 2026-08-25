class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        lst = []
        for i in nums:
            if i != min(nums) and i != max(nums):
                lst.append(i)
        if len(lst)==0:
            return -1
        return min(lst)