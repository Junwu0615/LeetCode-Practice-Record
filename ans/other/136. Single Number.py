"""
Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1
"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        record_list = []
        for i in nums:
            if i in record_list:
                record_list.remove(i)
            else:
                record_list += [i]
        return record_list[0]

if __name__ == '__main__':
    s = Solution()
    nums = [2,2,1]
    print(f'nums: {nums}, ans: {s.singleNumber(nums)}')

    nums = [4,1,2,1,2]
    print(f'nums: {nums}, ans: {s.singleNumber(nums)}')

    nums = [1]
    print(f'nums: {nums}, ans: {s.singleNumber(nums)}')