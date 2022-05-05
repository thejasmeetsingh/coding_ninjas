from sys import stdin, setrecursionlimit


class TrieNode():
    def __init__(self, char = '\0') :
        self.char = char
        self.isTerminal = False
        self.children = dict()


class Trie():
    def __init__(self) :
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
        self.insertWord(self.__root, word)
    
    
    def isPatternExists(self, root, pattern):
        if not pattern:
            return True
        
        child = root.children.get(pattern[0])
        
        if not child:
            return False
        return self.isPatternExists(child, pattern[1:])
    
    
    def isPalindromePair(self, word):
        return self.isPatternExists(self.__root, word)
                

def takeInput() :
    n = int(input())

    if n == 0 :
        return list(), 0

    li = list(map(str, stdin.readline().rstrip().split(" ")))
    return li, n


if __name__ == "__main__":
    listOfWords, n = takeInput()

    t = Trie()

    for _word in listOfWords:
        if _word == _word[::-1]:
            print("true")
            exit(0)

        for i in range(len(_word)):
            t.insert(_word[i:])


    for _word in listOfWords:
        if t.isPalindromePair(_word[::-1]):
            print("true")
            exit(0)

    print("false")
