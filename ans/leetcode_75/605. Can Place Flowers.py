class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        f, count = 0, 1
        for i in flowerbed:
            if not i:
                count += 1
            else:
                count = 0
            if count == 3:
                f += 1
                count = 1
        else:
            if count == 2:
                f += 1
        return True if n <= f else False