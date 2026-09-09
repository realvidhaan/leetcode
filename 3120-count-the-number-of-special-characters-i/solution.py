class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lst = []
        lst2 = []
        for i in word:
            if i.lower() in word and i.upper() in word:
                lst.append(i)
        for i in lst:
            if i.islower():
                lst2.append(i)
        return len(list(set(lst2)))