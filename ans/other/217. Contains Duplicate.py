"""
給定一個整數數組nums，傳回數組中true是否有任何值出現至少兩次false，以及每個元素是否不同。

範例 1：
輸入： nums = [1,2,3,1]
輸出： true
解釋：
元素 1 出現在索引 0 和 3 處。

範例 2：
輸入： nums = [1,2,3,4]
輸出： false
解釋：
所有元素都是不同的。

範例 3：
輸入： nums = [1,1,1,3,3,4,3,2,4,2]
輸出： true
"""
import copy
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3,1]
    print(f'nums: {nums}, ans: {s.containsDuplicate(nums)}')

    nums = [1,2,3,4]
    print(f'nums: {nums}, ans: {s.containsDuplicate(nums)}')

    nums = [1,1,1,3,3,4,3,2,4,2]
    print(f'nums: {nums}, ans: {s.containsDuplicate(nums)}')