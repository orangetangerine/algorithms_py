class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for i in range(len(s)-1, -1, -1):
            c = s[i]
            if len(stack) > 0:
                if c == 'C' and stack[-1] == 'D':
                    stack.pop()
                    continue
                if c == 'A' and stack[-1] == 'B':
                    stack.pop()
                    continue
            stack.append(c)
        return len(stack)


if __name__ == '__main__':
    s = Solution()
    print(s.minLength('ABFCACDB'))
