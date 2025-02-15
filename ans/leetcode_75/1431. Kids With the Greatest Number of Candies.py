class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ret = []
        check = sorted(candies)[-1]
        for i in candies:
            ret += [True] if i + extraCandies >= check else [False]
        return ret