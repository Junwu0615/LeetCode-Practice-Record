class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ret, count = '', 0
        for i, j in zip(word1, word2):
            ret += f'{i}{j}'
            count += 1
        if len(word1) != len(word2):
            ret += word1[count:] if len(word1) > len(word2) else word2[count:]
        return ret