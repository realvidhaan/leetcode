class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        lst = []
        for i, j in enumerate(sorted(nums)):
            if j==target:
                lst.append(i)
        return lst