class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        lst=[]
        for i in str(int("".join(map(str, digits)))+1):
            lst.append(int(i))
        return lst