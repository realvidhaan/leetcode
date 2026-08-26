class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        counter = 0
        for i in list(combinations(nums, 2)):
            if sum(i)<target:
                counter+=1
        return counter