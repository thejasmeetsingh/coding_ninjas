def zigzagOrder(root):
    if not root:
        return
    
    q = queue.Queue()
    q.put(root)
    level = 1
    
    while not q.empty():
        nodes = []
        for _ in range(q.qsize()):
            nodes.append(q.get())
            
            if nodes[-1].left:
                q.put(nodes[-1].left)
            if nodes[-1].right:
                q.put(nodes[-1].right)
        
        if level % 2 == 0:
            while nodes:
                print(nodes.pop().data, end=" ")
        else:
            while nodes:
                print(nodes.pop(0).data, end=" ")
        
        print()
        level += 1
