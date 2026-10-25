class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        lst = []
        for i in range(left, right+1):
            counter = 0
            for j in str(i):
                if int(j)!=0 and i%int(j)==0:
                    counter+=1
            if counter==len(str(i)):
                lst.append(i)
        return lst