class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        lst=[]
        for i in words:
            if i.startswith(pref):
                lst.append(i)
        return len(lst)