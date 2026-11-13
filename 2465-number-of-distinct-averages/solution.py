class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        lst=[]
        while len(nums)>1:
            lst.append((min(nums)+max(nums))/2)
            nums.remove(min(nums))
            nums.remove(max(nums))
        return len(set(lst))