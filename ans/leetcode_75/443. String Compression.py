class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        write, read = 0, 0
        while read < n:
            count = 0
            char = chars[read]

            while read < n and chars[read] == char:
                read += 1
                count += 1

            chars[write] = char
            write += 1

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        return write