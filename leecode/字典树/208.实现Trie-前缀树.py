# 方法一：
# from collections import defaultdict


# class Node():
#     def __init__(self):
#         self.children = defaultdict(Node)
#         self.is_word = False


# class Trie:

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.root = Node()

#     def insert(self, word: str) -> None:
#         """
#         Inserts a word into the trie.
#         """
#         # 当前节点为根节点
#         cur_node = self.root
#         for char in word:
#             # 当前节点更新为上一个字符串的子节点
#             cur_node = cur_node.children[char]
#         cur_node.is_word = True

#     def search(self, word: str) -> bool:
#         """
#         Returns if the word is in the trie.
#         """
#         cur_node = self.root
#         for char in word:
#             cur_node = cur_node.children.get(char)
#             if cur_node is None:
#                 return False
#         else:
#             return cur_node.is_word

#     def startsWith(self, prefix: str) -> bool:
#         """
#         Returns if there is any word in the trie that starts with the given prefix.
#         """
#         cur_node = self.root
#         for char in prefix:
#             cur_node = cur_node.children.get(char)
#             if cur_node is None:
#                 return False
#         else:
#             return True


# 方法二：
class TrieNode:
    def __init__(self):
        self.nodes = dict()
        self.is_leaf = False

    def insert(self, word: str):
        """ 插入一个词到字典树中 """
        curr = self
        for char in word:
            if char not in curr.nodes:
                curr.nodes[char] = TrieNode()
            curr = curr.nodes[char]
        curr.is_leaf = True

    def search(self, word: str):
        curr = self
        for char in word:
            if char not in curr.nodes:
                return False
            curr = curr.nodes[char]
        return curr.is_leaf

    def startsWith(self, prefix: str) -> bool:
        curr = self
        for char in prefix:
            if char not in curr.nodes:
                return False
            curr = curr.nodes[char]
        else:
            return True


tn = TrieNode()
tn.insert('python')
print(tn.search('python'))
print(tn.search('pyth'))
print(tn.startsWith('pyh'))
