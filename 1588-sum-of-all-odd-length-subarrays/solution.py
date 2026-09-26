class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        subarrays = []
        lst = []
        for start in range(len(arr)):
            for end in range(start, len(arr)):
                subarrays.append(arr[start:end + 1])
        for i in subarrays:
            if len(i)%2!=0:
                lst.append(sum(i))
        return sum(lst)