def getBSTData(root):
    if not root:
        return [10 ** 6, -1, True, 0]
    
    bst_data_left = getBSTData(root.left)
    bst_data_right = getBSTData(root.right)
    
    min_node = min(root.data, min(bst_data_left[0], bst_data_right[0]))
    max_node = max(root.data, max(bst_data_left[1], bst_data_right[1]))
    is_bst = root.data > bst_data_left[1] and root.data < bst_data_right[0] and bst_data_left[2] and bst_data_right[2]
    
    if is_bst:
        height = 1 + max(bst_data_left[3], bst_data_right[3])
    else:
        height = max(bst_data_left[3], bst_data_right[3])
    
    return [min_node, max_node, is_bst, height]

        
def largestBSTSubtree(root):
    if not root:
        return 0
    
    result = getBSTData(root)
    return result[3]
