"""
給你一個數組prices，其中prices[i]表示當天某檔股票的價格。ith
您希望透過選擇某一天購買一隻股票並選擇未來的另一天出售該股票來實現利潤最大化。
返回本次交易您所能獲得的最大利潤。如果您無法獲得任何利潤，則返回0。

範例 1：
輸入： prices = [7,1,5,3,6,4]
輸出： 5
解釋：第 2 天買入（價格 = 1），第 5 天賣出（價格 = 6），利潤 = 6-1 = 5。
請注意，不允許在第 2 天買入並在第 1 天賣出，因為您必須先買入再賣出。

範例 2：
輸入： prices = [7,6,4,3,1]
輸出： 0
解釋：在這種情況下，沒有進行任何交易，最大利潤 = 0。
"""
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pass

if __name__ == '__main__':
    s = Solution()
    prices = [7,1,5,3,6,4]
    print(f'prices: {prices}, ans: {s.maxProfit(prices)}')

    prices = [7,6,4,3,1]
    print(f'prices: {prices}, ans: {s.maxProfit(prices)}')