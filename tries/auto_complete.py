class TrieNode():
    def __init__(self, char='\0'):
        self.char = char
        self.terminal = False
        self.children = {}

        
class Trie():
    def __init__(self):
        self.__root = TrieNode()
        self.numWords = 0

        
    def insertWord(self, word):
        curr = self.__root
        for char in word:
            if char in curr.children:
                curr = curr.children[char]
            else:
                curr.children[char] = TrieNode(char)
                curr = curr.children[char]
        curr.terminal = True
        self.numWords = self.numWords + 1
    
    
    def search(self, word):
        if not word:
            return False
        
        curr = self.__root
        
        for char in word:
            if not curr.children.get(char):
                return False
            curr = curr.children[char]
        return curr
        
    
    def autoCompleteUtil(self, root, word, result):
        if root.terminal:
            print(result)
        
        for key in root.children:
            self.autoCompleteUtil(root.children[key], word, result + root.children[key].char)


    def autoComplete(self, input,  pattern):
        for word in input:
            self.insertWord(word)
        
        node = self.search(pattern)
        
        if not node:
            return
        
        if not node.children:
            if node.terminal:
                print(pattern)
            return
        
        self.autoCompleteUtil(node, pattern, pattern)
