class Solution:
    def minLength(self, s: str) -> int:
        stack = ['']  # 提前塞个空串, 后面可以不用判断是不是空
        for c in s:
            if (c == 'D' and stack[-1] == 'C') or (c == 'B' and stack[-1] == 'A'):
                stack.pop()
            else:
                stack.append(c)
        return len(stack) - 1


if __name__ == '__main__':
    s = Solution()
    print(s.minLength('ABFCACDB'))
