class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp, count = [], 0
        for i in nums:
            if i == 0:
                count += 1
            else:
                temp += [i]
        todo = temp + [0] * count
        count = 0
        for i in todo:
            nums[count] = i
            count += 1