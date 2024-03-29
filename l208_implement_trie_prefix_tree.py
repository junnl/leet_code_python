

class Trie:

    def __init__(self):
        self.data = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        tree = self.data
        for a in word:
            if a not in tree:
                tree[a] = {}
            tree = tree[a]
        tree["#"] = "#"

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        tree = self.data
        for a in word:
            if a not in tree:
                return False
            tree = tree[a]
        if "#" in tree:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tree = self.data
        for a in prefix:
            if a not in tree:
                return False
            tree = tree[a]
        return True



