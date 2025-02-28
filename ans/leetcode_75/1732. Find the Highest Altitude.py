class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ret, count = 0, 0
        for i in gain:
            count += i
            ret = max(ret, count)
        return ret