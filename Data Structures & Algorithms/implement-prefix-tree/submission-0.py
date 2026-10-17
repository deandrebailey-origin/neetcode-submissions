class TNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class PrefixTree:

    def __init__(self):
        self.root = TNode()


    def insert(self, word: str) -> None:
        node = self.root
        final = ''
        for c in word:
            if not node.children.get(c):
                node.children[c] = TNode()
            node = node.children[c]
            final = c
        node.isEnd = True


    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if not node.children.get(c):
                return False
            node = node.children[c]
            final = c
        return node.isEnd 

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if not node.children.get(c):
                return False
            node = node.children[c]
        return True
        
        