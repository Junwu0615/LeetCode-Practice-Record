"""
TODO
        給定一串數字num，例如"123456579"。我們可以將其拆分成類似斐波那契的序列[123, 456, 579]。
        形式上，類斐波那契數列是一串f非負整數，滿足：
        0 <= f[i] < 231，（也就是說，每個整數都適合32 位元有符號整數類型），
        f.length >= 3， 和
        f[i] + f[i + 1] == f[i + 2]為所有人0 <= i < f.length - 2。
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
        return [num]


if __name__ == '__main__':
    s = Solution()
    q = "1101111"
    print(f'q: {q}, ans: {s.splitIntoFibonacci(q)}')

    q = "112358130"
    print(f'q: {q}, ans: {s.splitIntoFibonacci(q)}')

    q = "0123"
    print(f'q: {q}, ans: {s.splitIntoFibonacci(q)}')