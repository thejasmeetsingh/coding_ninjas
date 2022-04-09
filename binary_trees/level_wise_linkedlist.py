def constructLinkedListForEachLevel(root):
    if not root:
        return None
    
    result = []
    q = queue.Queue()
    q.put(root)
    
    while not q.empty():
        nodes = []
        for _ in range(q.qsize()):
            node = q.get()
            linked_list_node = Node(node.data)
            
            if nodes:
            	nodes[-1].next = linked_list_node
            nodes.append(linked_list_node)
            
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)
        
        result.append(nodes[0] if nodes else None)
    
    return result
