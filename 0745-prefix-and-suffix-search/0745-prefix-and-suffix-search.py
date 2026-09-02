class Node:
    def __init__(self):
        self.children = {}
        self.idx = -1


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word, idx):
        node = self.root

        for i in word:
            if i not in node.children:
                node.children[i] = Node()

            node = node.children[i]
            node.idx = max(node.idx, idx)

    def search(self, word):
        node = self.root

        for i in word:
            if i not in node.children:
                return -1

            node = node.children[i]

        return node.idx


class WordFilter:
    def __init__(self, words: List[str]):
        self.t = Trie()

        for idx, w in enumerate(words):
            for i in range(len(w)):
                k = w[i:] + '#' + w
                self.t.insert(k, idx)

    def f(self, pref: str, suff: str) -> int:
        return self.t.search(suff + '#' + pref)