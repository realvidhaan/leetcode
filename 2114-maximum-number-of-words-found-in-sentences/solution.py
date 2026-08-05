class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        lst = []
        for i in sentences:
            lst.append(i.count(" ")+1)
        return max(lst)