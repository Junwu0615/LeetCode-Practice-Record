"""
TODO
        如果滿足以下條件，則該序列為類斐波那契序列：x1, x2, ..., xn
            n >= 3
            xi + xi+1 == xi+2為所有人 i + 2 <= n
        給定一個嚴格遞增的 arr 正整數數組，組成一個序列，傳回的最長斐波那契子序列的長度 arr。如果不存在，則傳回 0。
        子序列是從另一個序列中得到的，arr方法是從中刪除任意數量的元素（包括零）arr，而不改變剩餘元素的順序。
        例如，[3, 5, 8] 是的子序列 [3, 4, 5, 6, 7, 8]。
TODO
        輸入： arr = [1,2,3,4,5,6,7,8]
        輸出： 5
        解釋：最長的斐波那契子序列：[1,2,3,5,8]。
TODO
        輸入： arr = [1,3,7,11,12,14,18]
        輸出： 3
        解釋： 最長的斐波那契子序列：[1,11,12]、[3,11,14] 或 [7,11,18]。
"""
from typing import List


class Solution:
    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        N = len(arr)
        # 1. 预处理：创建元素到索引的映射，实现 O(1) 查找
        index_map = {value: i for i, value in enumerate(arr)}

        # 2. DP 表：dp[(i, j)] 存储以 arr[i] 和 arr[j] 结尾的最长斐波那契子序列的长度
        # 初始值设为 2，因为任何一对 (arr[i], arr[j]) 至少是长度为 2 的序列
        dp = {}
        max_len = 0

        # 3. 迭代所有可能的结尾对 (arr[i], arr[j])
        for j in range(N):
            for i in range(j):
                # arr[i] 是序列的倒数第二个元素，arr[j] 是倒数第一个元素

                # 计算目标值 arr[k]，即 arr[j] - arr[i]
                target = arr[j] - arr[i]

                # 4. 查找 arr[k]
                # 必须满足 arr[k] < arr[i]（因为 k < i），所以 target < arr[i]
                if target < arr[i]:
                    # 在 O(1) 时间内查找 target 的索引 k
                    if target in index_map:
                        k = index_map[target]

                        # 5. 更新 DP：dp[(i, j)] = dp[(k, i)] + 1
                        # 检查 dp[(k, i)] 是否已计算
                        # 如果 dp[(k, i)] 存在，则序列长度加 1
                        if (k, i) in dp:
                            dp[(i, j)] = dp[(k, i)] + 1
                        else:
                            # 第一次找到 (k, i, j) 序列，长度为 3
                            dp[(i, j)] = 3

                        # 更新最大长度
                        max_len = max(max_len, dp[(i, j)])

                # 否则，arr[i] 和 arr[j] 只能是长度为 2 的起始对，
                # dp[(i, j)] 保持为 0 (或不存入字典，因为我们只关心长度 >= 3 的序列)。

        return max_len


if __name__ == '__main__':
    s = Solution()
    q = [1,2,3,4,5,6,7,8]
    print(f'q: {q}, ans: {s.lenLongestFibSubseq(q)}')

    q = [1,3,7,11,12,14,18]
    print(f'q: {q}, ans: {s.lenLongestFibSubseq(q)}')