class Solution:
    def countElements(self, nums: List[int]) -> int:
        if len(set(nums))==1:
            return 0
        return len(nums)-nums.count(min(nums))-nums.count(max(nums))