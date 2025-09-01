class Trie:

    def __init__(self):
        self.trie = [[0]*27]

    def insert(self, word: str) -> None:
        curr = self.trie[0]
        for x in word:
            index = ord(x)-ord('a')+1
            if curr[index] == 0:
                curr[index] = len(self.trie)
                self.trie.append([0]*27)
            curr = self.trie[curr[index]]
        curr[0] = 1

    def search(self, word: str) -> bool:
        curr = self.trie[0]
        for x in word:
            index = ord(x)-ord('a')+1
            if not curr[index]:
                return False
            curr = self.trie[curr[index]]
        if curr[0]==1:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        curr = self.trie[0]
        for x in prefix:
            index = ord(x)-ord('a')+1
            if curr[index]==0:
                return False
            curr = self.trie[curr[index]]
        return True
