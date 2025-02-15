class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ret = []
        check = sorted(candies)[-1]
        for i in candies:
            if i + extraCandies >= check:
                ret += [True]
            else:
                ret += [False]
        return ret