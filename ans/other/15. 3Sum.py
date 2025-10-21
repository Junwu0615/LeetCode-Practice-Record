"""
"""
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pass

if __name__ == '__main__':
    s = Solution()
    nums = [3,0,1]
    print(f'nums: {nums}, ans: {s.missingNumber(nums)}')

    nums = [0,1]
    print(f'nums: {nums}, ans: {s.missingNumber(nums)}')

    nums = [9,6,4,2,3,5,7,0,1]
    print(f'nums: {nums}, ans: {s.missingNumber(nums)}')