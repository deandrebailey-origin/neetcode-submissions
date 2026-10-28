class Node:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if not node.children.get(c):
                node.children[c] = Node()
            node = node.children[c]
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.root
        

        def dfs(node, i) -> bool:
            if i == len(word):
                return node.isEnd
            

            if word[i] == '.':
                for key in node.children:
                    if dfs(node.children[key], i+1):
                        return True
                return False
            if not node.children.get(word[i]):
                return False
            node = node.children[word[i]]
            return dfs(node, i + 1)

        return dfs(node, 0)

            
            

            

        
