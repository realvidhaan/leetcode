class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr = sorted(nums)
        for i in range(0, len(arr) - 1, 2):
            arr[i], arr[i + 1] = arr[i + 1], arr[i]  
        return arr