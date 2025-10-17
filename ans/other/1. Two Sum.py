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
        for idx_out, v in enumerate(nums):
            check = target - v
            if check in nums:
                if nums.index(check) != idx_out:
                    return sorted([idx_out, nums.index(check)])
            # for idx_in, i in enumerate(nums[idx_out + 1:]):
            #     if i == check:
            #         return [idx_out, idx_in + idx_out + 1]


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