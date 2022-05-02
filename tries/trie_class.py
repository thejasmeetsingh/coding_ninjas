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

    
    def remove_word(self, root, word):
        if not word:
            root.terminal = False
            return

        child = root.children.get(word[0])
        if not child:
            return

        self.remove_word(child, word[1:])

        if not child.terminal and not child.children:
            root.children.pop(word[0])
            del child

        return

    def remove(self, word):
        self.remove_word(self.root, word)
