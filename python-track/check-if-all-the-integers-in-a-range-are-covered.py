class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        nums = {i for i in range(left, right+1)}
        range_set = set()
        for i in ranges:
            temp = {x for x in range(i[0], i[1]+1)}
            range_set = range_set | temp
        if nums <= range_set:
            return True
        return False