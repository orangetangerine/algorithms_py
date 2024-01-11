class Solution:
    # 动态规划
    def addMinimum(self, word: str) -> int:
        d = [0] * (len(word) + 1)
        for i in range(1, len(word) + 1):
            d[i] = d[i - 1] + 2  # 3个一组, 假设这个字符单独一组,则缺2
            w_idx = i - 1
            # 当前字符比上一个大, 无论大多少, 凑成一组的所需要的数量都可以少一个了
            if w_idx > 0 and word[w_idx] > word[w_idx - 1]:
                d[i] = d[i - 1] - 1
        return d[len(word)]

    def addMinimum2(self, word: str) -> int:
        # word = 'abc'+word+'abc'
        group = ord('c') - ord('a') + 1  # 一组有3个字符(abc)
        count = 0
        #  处理每两个字符中间, 需要添多少个字符
        for i in range(1, len(word)):
            count += (ord(word[i]) - ord(word[i - 1]) - 1 + group) % group
        # 剩下头尾两个字符, 看看前后是否需要添加字符
        # 第一个字符, 看看前面是否要加东西; 如果一开始word = 'abc'+word, 则可以不处理第一个字符
        count += ord(word[0]) - ord('a')
        # 最后一个字符, 看看后面是否要加东西; 如果一开始word += 'abc', 则可以不处理最后这个字符
        count += ord('c') - ord(word[-1])
        return count


if __name__ == '__main__':
    s = Solution()
    for w in ['abcc', 'b', 'ac', 'c', 'aac', 'ca', 'aaaabb', 'bb', 'cc']:
        print(w, s.addMinimum(w), s.addMinimum2(w))
