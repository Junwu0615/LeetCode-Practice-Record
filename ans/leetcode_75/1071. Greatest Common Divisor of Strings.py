class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1[:min(len(str1), len(str2))] != str2[:min(len(str1), len(str2))]:
            return ''
        for i in range(min(len(str1), len(str2)), 0, -1):
            x = str1[:i]
            if str1.replace(x, '') == '' and str2.replace(x, '') == '':
                return x
        return ''