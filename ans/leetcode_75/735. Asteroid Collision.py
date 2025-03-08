class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ret = []
        for i in asteroids:
            while ret and i < 0 and ret[-1] > 0:
                diff = i + ret[-1]
                if diff < 0:
                    ret.pop()
                elif diff > 0:
                    i = 0
                else:  # diff == 0
                    ret.pop()
                    i = 0
            if i != 0:
                ret.append(i)
        return ret