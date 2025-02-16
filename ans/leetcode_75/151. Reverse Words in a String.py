class Solution:
    def reverseWords(self, s: str) -> str:
        def trans_fun(todo: str):
            if todo[0] == ' ':
                todo = todo[1:]
            if todo[-1] == ' ':
                todo = todo[:-1]
            return todo

        temp = [i for i in s.split(' ') if i != '']
        ret = ''
        for idx in range(len(temp) - 1, -1, -1):
            ret += f'{temp[idx]} '
        return trans_fun(ret)