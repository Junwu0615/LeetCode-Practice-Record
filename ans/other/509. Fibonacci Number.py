"""
TODO
        斐波那契數列，通常表示為 ，F(n)它構成一個數列，稱為斐波那契數列，其中每個數都是前兩個數之和，從0和開始1。也就是說，
TODO
        F(0) = 0, F(1) = 1
        F(n) = F(n - 1) + F(n - 2)，其中 n > 1
        已知n，計算F(n)
TODO
        輸入： n = 2
        輸出： 1
        解釋： F(2) = F(1) + F(0) = 1 + 0 = 1
TODO
        輸入： n = 3
        輸出： 2
        解釋： F(3) = F(2) + F(1) = 1 + 1 = 2
TODO
        輸入： n = 4
        輸出： 3
        解釋： F(4) = F(3) + F(2) = 2 + 1 = 3

TODO
        最優解通常是使用動態規劃（Dynamic Programming）或迭代的方法，因為這兩種方法都能達到 O(n) 的時間複雜度
"""
class Solution:
    def __init__(self):
        self.mapping_dict = {}
        self.mapping_dict = self.mapping_process()

    def mapping_process(self):
        mapping_dict = {}
        for key in range(0, 10):
            mapping_dict[key] = self.fib(key)
        return mapping_dict


    def fib(self, n: int) -> int:
        # 法一
        # if n == 0:
        #     return 0
        # elif n == 1:
        #     return 1
        # else:
        #     return self.fib(n - 1) + self.fib(n - 2)

        # 法二
        if n in self.mapping_dict:
            return self.mapping_dict[n]
        else:
            if n in [0, 1]:
                return 0 if n == 0 else 1
            else:
                return self.fib(n - 1) + self.fib(n - 2)


if __name__ == '__main__':
    s = Solution()
    q = 2
    print(f'q: {q}, ans: {s.fib(q)}')

    q = 3
    print(f'q: {q}, ans: {s.fib(q)}')

    q = 4
    print(f'q: {q}, ans: {s.fib(q)}')