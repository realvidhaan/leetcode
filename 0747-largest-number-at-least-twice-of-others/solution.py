class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        cntr = 0
        for i in nums:
            if max(nums)>=i*2:
                cntr+=1
        if cntr == len(nums)-1:
            return nums.index(max(nums))
        return -1