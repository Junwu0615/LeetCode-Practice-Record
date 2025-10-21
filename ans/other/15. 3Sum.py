"""
"""
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res: List[List[int]] = []
        if n < 3:
            return res

        nums.sort()  # 先排序 O(n log n)

        for i in range(n - 2):
            # 跳過重複的第一個元素
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 如果當前 nums[i] 已經 > 0，三數和不可能為 0（因為後面皆 ≥ nums[i]）
            if nums[i] > 0:
                break

            target = -nums[i]
            left, right = i + 1, n - 1

            while left < right:
                s = nums[left] + nums[right]
                if s == target:
                    res.append([nums[i], nums[left], nums[right]])

                    # 跳過左邊重複值
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # 跳過右邊重複值
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # 兩指針向內移動繼續尋找
                    left += 1
                    right -= 1
                elif s < target:
                    left += 1
                else:
                    right -= 1

        return res

if __name__ == '__main__':
    s = Solution()
    nums = [-1,0,1,2,-1,-4]
    print(f'nums: {nums}, ans: {s.threeSum(nums)}')

    nums = [0,1,1]
    print(f'nums: {nums}, ans: {s.threeSum(nums)}')

    nums = [0,0,0]
    print(f'nums: {nums}, ans: {s.threeSum(nums)}')