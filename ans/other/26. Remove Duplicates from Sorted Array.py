"""
範例 1：
輸入： nums = [1,1,2]
輸出： 2, nums = [1,2,_]
解釋：你的函數應該回傳 k = 2，其中 nums 的前兩個元素分別為 1 和 2。
除了返回的 k 之外留下什麼都沒有關係（因此它們是下劃線）。

範例 2：
輸入： nums = [0,0,1,1,1,2,2,3,3,4]
輸出： 5, nums = [0,1,2,3,4,_,_,_,_,_]
解釋：你的函數應該傳回 k = 5，其中 nums 的前五個元素分別為 0、1、2、3 和 44。
除了返回的 k 之外留下什麼都沒有關係（因此它們是下劃線）。
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        slow = 0
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1
        # nums = list(set(nums))
        # return len(nums)

if __name__ == '__main__':
    s = Solution()
    nums = [1,1,2]
    print(f'nums: {nums}, ans: {s.removeDuplicates(nums)}')

    nums = [0,0,1,1,1,2,2,3,3,4]
    print(f'nums: {nums}, ans: {s.removeDuplicates(nums)}')