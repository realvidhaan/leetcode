class Solution:
    def convertDateToBinary(self, date: str) -> str:
        nums=date.split("-")
        ting=""
        for i in nums:
            ting+=bin(int(i)).replace("0b", "")
            ting+="-"
        return ting.rstrip("-")