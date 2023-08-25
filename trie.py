class TrieNode:
    def __init__(self) -> None:
        self.childern = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.data = []
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.childern:
                curr.childern[char] = TrieNode()
            curr = curr.childern[char]
        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.childern:
                return False
            curr = curr.childern[char]
        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.childern:
                return False
            curr = curr.childern[char]
        return True


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("apple")
print(obj.search("apple"))
print(obj.startsWith("appo"))

# param_3 = obj.startsWith(prefix)
