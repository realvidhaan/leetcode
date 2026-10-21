class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lst = []
        for i, j in enumerate(sorted(nums)):
            if j==target:
                lst.append(i)
        if len(lst)==0:
            return [-1, -1]
        if len(lst)==1:
            return [nums.index(target), nums.index(target)]
        return [lst[0], lst[-1]]