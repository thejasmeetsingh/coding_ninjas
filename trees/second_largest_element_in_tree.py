def secondLargestUtil(tree):
    if not tree:
        return None, None
    
    largest_node = tree
    second_largest_node = None
    
    for child in tree.children:
        _largest_node, _second_largest_node = secondLargestUtil(child)
        
        if _largest_node and _largest_node.data > largest_node.data:
            second_largest_node = largest_node
            largest_node = _largest_node
            
        if not second_largest_node or (_largest_node and largest_node.data < _largest_node.data < second_largest_node.data):
            second_largest_node = _largest_node
            
        if not second_largest_node or (_second_largest_node and _second_largest_node.data > second_largest_node.data):
            second_largest_node = _second_largest_node
    
    return largest_node, second_largest_node


def secondLargest(tree):
    if not tree:
        return None
    
    largest_node, second_largest_node = secondLargestUtil(tree)
    return second_largest_node if second_largest_node and largest_node.data > second_largest_node.data else None
