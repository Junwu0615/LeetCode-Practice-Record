class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_num = 0
        cur_string = ''
        for char in s:
            if char == '[':
                stack += [cur_string]
                stack += [cur_num]
                cur_string = ''
                cur_num = 0
            elif char == ']':
                num = stack.pop()
                prev_string = stack.pop()
                cur_string = prev_string + num * cur_string
            elif char.isdigit():
                cur_num = cur_num * 10 + int(char)
            else:
                cur_string += char
        return cur_string