from sys import stdin
import sys

sys.setrecursionlimit(10 ** 8)

class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        
    def __str__(self):
        return str(self.data)

def find_height(root):
    height = 0
    
    if not root:
        return 0
    
    if len(root.children) == 0:
        return 1
    
    for child in root.children:
        height = max(height, find_height(child))
    
    return height + 1


def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i<size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0,childCount):
            temp = treeNode(int(arr[i+j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root

# Main
arr = list(int(x) for x in stdin.readline().rstrip().rsplit())
tree = createLevelWiseTree(arr)
print(find_height(tree))
