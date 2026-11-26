class Solution:
    def bitwiseComplement(self, n: int) -> int:
        lst=[]
        for i in bin(n).replace("0b", ""):
            lst.append(str(1-int(i)))
        return int("".join(lst), 2)
        