class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        lst = []
        for i in nums:
            if i%2==0:
                lst.append(i)
        if len(lst)==0:
            return -1
        max_count = max(map(lst.count, lst))  
        return min(list(set([x for x in lst if lst.count(x) == max_count])))