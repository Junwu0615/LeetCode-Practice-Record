class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        idx = min(len(str1), len(str2))
        if str1[:idx] != str2[:idx]:
            return ''
        for i in range(idx, 0, -1):
            check = str1[:i]
            if str1.replace(check, '') == '' and str2.replace(check, '') == '':
                return check
        return ''