"""
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
"""
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[num] = i


if __name__ == '__main__':
    s = Solution()
    nums = [2,7,11,15]
    target = 9
    print(f'nums: {nums}, target: {target}, ans: {s.twoSum(nums, target)}')

    nums = [3,2,4]
    target = 6
    print(f'nums: {nums}, target: {target}, ans: {s.twoSum(nums, target)}')

    nums = [3,3]
    target = 6
    print(f'nums: {nums}, target: {target}, ans: {s.twoSum(nums, target)}')