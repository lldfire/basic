# 方法一：字典树 + 递归DFS
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.node = dict()
        # self.end = False

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        curr = self.node
        for char in word:
            if char not in curr:
                curr[char] = dict()
            curr = curr[char]
        curr['end'] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        # curr = self
        # for char in word:
        #     if char not in curr.node:
        #         return False
        #     curr = curr.node[char]
        cut = False

        def helper(curr_dict, chars):
            nonlocal cut
            if cut:
                return True
            curr = curr_dict
            for i, char in enumerate(chars):
                if char == '.':
                    return any(helper(
                        curr[j], chars[i + 1:]) for j in curr if j != 'end')
                if char not in curr:
                    return False
                curr = curr[char]
            cut = 'end' in curr
            return cut
        return helper(self.node, word)


# 方法二：字典树 + 非递归DFS


# 方法三：优化的字典树
        
if __name__ == '__main__':
    wd = WordDictionary()
    # word = 'dad'
    wd.addWord('a')
    wd.addWord('ab')
    # wd.addWord('dad')
    print(wd.search('.b'))
    # print(wd.search('ab'))
    # print(wd.search('.ad'))
    # print(wd.search('..'))
    