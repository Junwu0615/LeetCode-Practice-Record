class Solution:
    def reverseVowels(self, s: str) -> str:
        ret = ''
        check = ['a', 'e', 'i', 'o', 'u']
        temp = [i for i in s if i.lower() in check]
        for i in s:
            if i.lower() in check:
                ret += temp[-1]
                temp.pop(-1)
            else:
                ret += i
        return ret