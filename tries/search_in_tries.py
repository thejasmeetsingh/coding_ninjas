class TrieNode():
    def __init__(self, char='\0'):
        self.char = char
        self.terminal = False
        self.children = dict()
        
class Trie():
    def __init__(self):
        self.__root = TrieNode()

    def insert(self, word):
        curr = self.__root
        for char in word:         
            if not curr.children.get(char):
                curr.children[char] = TrieNode(char)
            curr = curr.children[char]

        curr.terminal = True

    def search(self, word):
        if not word:
            return False
        
        curr = self.__root
        for char in word:
            if not curr.children.get(char):
                return False
            curr = curr.children[char]
        
        return curr.terminal
