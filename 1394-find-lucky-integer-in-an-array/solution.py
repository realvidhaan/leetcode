class Solution:
    def findLucky(self, arr: List[int]) -> int:
        lst = []
        for i in arr:
            if arr.count(i)==i:
                lst.append(i)
        if len(lst)>0:
            return max(lst)
        return -1