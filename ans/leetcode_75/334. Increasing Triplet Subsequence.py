class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        small1 = float('inf')
        small2 = float('inf')
        for num in nums:
            if num <= small1:
                small1 = num
            elif num <= small2:
                small2 = num
            else:
                return True
        return False