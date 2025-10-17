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

TODO
    XOR 性質：
        a ^ a = 0
        a ^ 0 = a
        XOR 具交換律與結合律
        因此，若每個數字都出現兩次，唯一出現一次的那個會被「保留下來」
"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # record_list = []
        # for i in nums:
        #     if i in record_list:
        #         record_list.remove(i)
        #     else:
        #         record_list += [i]
        # return record_list[0]

        result = 0
        for n in nums:
            ori = result
            result ^= n # XOR：相同為 0，不同為 1
            print(f'{ori} ^= {n} = {result}')
        return result

if __name__ == '__main__':
    s = Solution()
    nums = [2,2,1]
    print(f'nums: {nums}, ans: {s.singleNumber(nums)}')

    nums = [4,1,2,1,2]
    print(f'nums: {nums}, ans: {s.singleNumber(nums)}')

    nums = [1]
    print(f'nums: {nums}, ans: {s.singleNumber(nums)}')