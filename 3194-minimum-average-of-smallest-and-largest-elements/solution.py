class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        av = []
        for i in range(len(nums)//2):
            av.append(((min(nums)+max(nums))/2))
            nums.remove(min(nums))
            nums.remove(max(nums))
        return min(av)