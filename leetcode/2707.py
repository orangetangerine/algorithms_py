
class Solution:
    def minExtraChar(self, s: str, dictionary: list[str]) -> int:
        # 初始化cost数组, 最大cost为s的长度(完全不能分割), 用[maxint]也一样的
        # cost: 到这个位置, 分割后剩下的字符数量 (就是题目所求的值)
        d = [len(s)] * (len(s)+1)
        d[0] = 0
        # O(n), 初始化字典set
        dic = set()
        max_dic_len = 0  # 字典里面最长的单词的长度, 算是一个优化
        for w in dictionary:
            dic.add(w)
            max_dic_len = max(max_dic_len, len(w))
        # 动态规划
        for i in range(1, len(s)+1):
            d[i] = d[i-1]+1  # i位置的初始值, 为上一个位置的cost+1
            for j in range(i-1, i-1-max_dic_len, -1):
                if s[j:i] in dic:
                    # 当前分割的cost, 是上一次的分法好呢, 还是用这一次的s[j:i]分法好呢, 取最小值
                    # 也不用记住怎么分的, 记住cost就行
                    d[i] = min(d[i], d[j])
        return d[len(s)]
class Solution2:
    #  递归+剪枝也可以的应该, 但是这里没剪好(没剪完), 超时了
    def minExtraCharUnknown(self, s: str, dictionary: list[str]) -> int:
        count = 0
        for i in range(len(s)):
            r = []
            for m in dictionary:
                if s[i:i+len(m)] == m:
                    if i+len(m) == len(s):
                        r.append(0)
                        break
                    else:
                        r.append(min(self.minExtraChar(s[i+len(m):], dictionary), 1+self.minExtraChar(s[i+1:], dictionary)))
            if len(r) == 0:
                count += 1
                continue
            count += min(r)
            break
        return count


if __name__ == '__main__':
    s = Solution()
    print(s.minExtraChar('octncmdbgnxapjoqlofuzypthlytkmchayflwky', ["m","its","imaby","pa","ijmnvj","k","mhka","n","y","nc","wq","p","mjqqa","ht","dfoa","yqa","kk","pixq","ixsdln","rh","dwl","dbgnxa","kmpfz","nhxjm","wg","wky","oct","og","uhin","zxb","qz","tpf","hlrc","j","l","tew","xbn","a","uzypt","uvln","mchay","onnbi","hlytk","pjoqlo","dxsjr","u","uj"]))
