"""
TODO
        給定一串數字num，例如"123456579"。我們可以將其拆分成類似斐波那契的序列[123, 456, 579]。
        形式上，類斐波那契數列是一串f非負整數，滿足：
        0 <= f[i] < 231，（也就是說，每個整數都適合 32 位元有符號整數類型），
        f.length >= 3， 和 f[i] + f[i + 1] == f[i + 2]為所有人0 <= i < f.length - 2。
        請注意，將字串拆分成幾個部分時，每個部分都不能有多餘的前導零，除非該部分是數字0本身。
        傳回從中分離出的任何類似斐波那契的序列，如果無法完成num則傳回 []
TODO
        輸入： num = "1101111"
        輸出： [11,0,11,11]
        解釋：輸出 [110, 1, 111] 也會被接受。
TODO
        輸入： num = "112358130"
        輸出： []
        解釋：此任務不可能完成。
TODO
        輸入： num = "0123"
        輸出： []
        解釋：不允許使用前導零，因此「01」、「2」、「3」無效。
TODO

"""
from typing import List


class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        _n = len(num)
        ans = []
        __int_max = 2 ** 31 - 1

        # 回溯函数：
        # start_index: 当前数字开始分割的位置
        def backtrack(start_index):
            # 1. 基本情况 (Base Case)：
            # 如果已遍历完整个字符串，并且序列长度至少为 3，则找到一个有效解。
            if start_index == _n:
                return len(ans) >= 3

            # 2. 遍历所有可能的下一个数字的结束位置
            # 最多取 10 位数字，因为 2^31-1 是 10 位数
            for i in range(start_index, _n):
                # 2.1 剪枝 1：处理前导零
                # 如果当前数字是多位数 (i > start_index)，且以 '0' 开头，则跳出
                if num[start_index] == '0' and i > start_index:
                    break

                # 2.2 形成当前数字
                current_num = int(num[start_index: i + 1])

                # 2.3 剪枝 2：溢出检查
                if current_num > __int_max:
                    break

                # 2.4 剪枝 3 & 检查斐波那契性质
                # 如果序列中已有至少两个数字
                if len(ans) >= 2:
                    # 检查是否满足 F(i) = F(i-1) + F(i-2)
                    expected_sum = ans[-1] + ans[-2]

                    if current_num > expected_sum:
                        # 当前数字过大，不可能再找到解，直接跳出 (最重要的剪枝之一)
                        break
                    elif current_num < expected_sum:
                        # 当前数字太小，需要尝试更长的数字，继续下一轮循环
                        continue

                # 3. 做出选择：当前数字有效 (是前两个数之一，或是正确的和)
                ans.append(current_num)

                # 4. 递归探索：从当前数字的下一个位置继续
                if backtrack(i + 1):
                    return True  # 找到一个解就立即返回 True

                # 5. 撤销选择 (Backtrack)：如果当前路径没有找到解，则移除当前数字
                ans.pop()

            return False  # 遍历完所有可能分割，未找到解

        # 从字符串开头开始回溯
        backtrack(0)
        return ans


if __name__ == '__main__':
    s = Solution()
    q = "1101111"
    print(f'q: {q}, ans: {s.splitIntoFibonacci(q)}')

    q = "112358130"
    print(f'q: {q}, ans: {s.splitIntoFibonacci(q)}')

    q = "0123"
    print(f'q: {q}, ans: {s.splitIntoFibonacci(q)}')