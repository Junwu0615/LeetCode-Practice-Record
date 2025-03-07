class Solution:
    def removeStars(self, s: str) -> str:
        temp = []
        for i in s:
            if i == '*':
                temp.pop()
            else:
                temp += [i]
        ret = ''.join(temp)
        return ret