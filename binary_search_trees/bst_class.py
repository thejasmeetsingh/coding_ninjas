class BST:
    def __init__(self):
        self.root = None
        self.numNodes = 0
    
    def printTreeUtil(self, root):
        if not root:
            return
        
        result = str(root.data) + ':'
        if root.left:
            result += "L:{},".format(root.left.data)
        if root.right:
            result += "R:{}".format(root.right.data)
        print(result)
        self.printTreeUtil(root.left)
        self.printTreeUtil(root.right)
    
    
    def printTree(self):
        self.printTreeUtil(self.root)
    
    
    def search(self, data):
        if not self.root:
            return False
        
        root = self.root
        
        while root:
            if root.data == data:
                return True
            
            if root.data > data:
                root = root.left
            else:
                root = root.right
        
        return False
    

    def insertUtil(self, root, data):
        if not root:
            return BinaryTreeNode(data)
        
        
        if data <= root.data:
            root.left = self.insertUtil(root.left, data)
        elif data > root.data:
            root.right = self.insertUtil(root.right, data)
        
        return root
        
    def insert(self, data):
        self.root = self.insertUtil(self.root, data)
    
    def deleteUtil(self, root, data):
        if not root:
            return None
        
        if data > root.data:
            root.right = self.deleteUtil(root.right, data)
            return root
        elif data < root.data:
            root.left = self.deleteUtil(root.left, data)
            return root
        else:
            if not root.left and not root.right:
                return None
            elif root.left and not root.right:
                return root.left
            elif not root.left and root.right:
                return root.right
            else:
                node = root.right
                while node.left:
                    node = node.left
                
                root.data = node.data
                root.right = self.deleteUtil(root.right, node.data)
                return root
      
        
    def delete(self, data):
        if not self.root:
            return None
        self.root = self.deleteUtil(self.root, data)
    
    def count(self):
        return self.numNodes
