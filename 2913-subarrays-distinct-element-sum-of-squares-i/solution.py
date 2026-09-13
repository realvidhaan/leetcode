class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        subarrays = []
        lst = []
        lst2 = []
        for start in range(len(nums)):
            for end in range(start, len(nums)):
                subarrays.append(nums[start:end + 1])
        for i in subarrays:
            lst.append(len(list(set(i))))
        for i in lst:
            lst2.append(i**2)
        return sum(lst2)