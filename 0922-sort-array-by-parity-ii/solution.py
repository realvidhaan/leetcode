class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        for i in nums:
            if i%2==0:
                even.append(i)
            else:
                odd.append(i)
        return [x for pair in zip(even, odd) for x in pair]
