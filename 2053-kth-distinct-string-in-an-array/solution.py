class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        lst = []
        for i in arr:
            if arr.count(i)==1:
                lst.append(i)
        return lst[k - 1] if 1 <= k <= len(lst) else ""