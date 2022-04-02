def maxSumUtil(root, resNode, maxsum):

    if not root:
        return
 
    currsum = root.data
    count = len(root.children)
 
    for i in range(0, count):
        currsum += root.children[i].data
        resNode, maxsum = maxSumUtil(root.children[i], resNode, maxsum)
 
    if currsum > maxsum:
        resNode = root
        maxsum = currsum
     
    return resNode, maxsum
 
    
def maxSumNode(root):
    resNode, maxsum = treeNode(None), 0
    resNode, maxsum = maxSumUtil(root, resNode, maxsum)
    return resNode, maxsum
