class TrieNode():
    count = 0
    def __init__(self, char='\0'):
        self.char = char
        self.terminal = False
        self.children = {}
        TrieNode.count += 1

class Trie():
    def __init__(self):
        self.__root = TrieNode()
    
    def insertWord(self, root, word):
        curr = root
        for char in word:
            if char in curr.children:
                curr = curr.children[char]
            else:
                curr.children[char] = TrieNode(char)
                curr = curr.children[char]
        curr.terminal = True

    def insert(self, word):
        rev_word = word[::-1]
        
        for i in range(len(word)):
            self.insertWord(self.__root, word[i:])
            self.insertWord(self.__root, rev_word[i:])
        
        
    def search(self, word):
        curr = self.__root
        for char in word:
            if char not in curr.children:
                return False
            else:
                curr = curr.children[char]
        return True
    
    def isPatternExists(self, root, pattern):
        if not pattern:
            return True
        
        child = root.children.get(pattern[0])
        
        if not child:
            return False
        
        return self.isPatternExists(child, pattern[1:])

    
    def patternMatching(self, words, pattern):
        for word in words:
            self.insert(word)
            if self.isPatternExists(self.__root, pattern):
                return True
        return False
