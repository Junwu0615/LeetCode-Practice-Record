class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            left = nums[:count]
            right = nums[count+1:]
            if sum(left) == sum(right):
                return count
            count += 1
        else:
            return -1