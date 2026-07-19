class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        n = []
        for i in hours:
            if i >= target:
                n.append(1)
        return len(n)