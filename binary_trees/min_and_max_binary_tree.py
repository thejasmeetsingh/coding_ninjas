class Pair:
    def __init__(self, minimum, maximum) :
        self.minimum = minimum
        self.maximum = maximum


def getMinAndMax(root):
    if not root:
        return root
    
    result = Pair(10 ** 6, -1)
    
    q = queue.Queue()
    q.put(root)
    
    while not q.empty():
        node = q.get()
        result.minimum = min(result.minimum, node.data)
        result.maximum = max(result.maximum, node.data)
        
        if node.left:
            q.put(node.left)
        if node.right:
            q.put(node.right)
    
    return result
