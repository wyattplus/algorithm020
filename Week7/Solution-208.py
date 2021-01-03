class TrieNode:
    def __init__(self):
        self.child = [None for _ in range(26)]
        self.isEnd = False

    def contain_key(self, ch):
        return self.child[ord(ch) - ord('a')]

    def get(self, ch):
        return self.child[ord(ch) - ord('a')]

    def put(self, ch):
        self.child[ord(ch) - ord('a')] = TrieNode()


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        p = self.root
        for c in word:
            if not p.contain_key(c):
                p.put(c)
            p = p.get(c)
        p.isEnd = True

    def search(self, word: str) -> bool:
        p = self.root
        for c in word:
            if not p.contain_key(c):
                return False
            else:
                p = p.get(c)
        return p.isEnd

    def startsWith(self, prefix: str) -> bool:
        p = self.root
        for c in prefix:
            if not p.contain_key(c):
                return False
            else:
                p = p.get(c)
        return True
