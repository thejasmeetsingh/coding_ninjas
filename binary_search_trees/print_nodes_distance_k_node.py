def printNodeFromKDistrance(root, k):
    if not root:
        return None
    
    if k == 0:
        print(root.data)
        return
    
    printNodeFromKDistrance(root.left, k - 1)
    printNodeFromKDistrance(root.right, k - 1)

    
def printNodes(root, node, k):
    if not root:
        return -1
    
    if root.data == node:
        printNodeFromKDistrance(root, k)
        return 0
    
    left_distance = printNodes(root.left, node, k)
    
    if left_distance == -1:
        right_distance = printNodes(root.right, node, k)
        
        if right_distance == -1:
            return -1
        elif right_distance + 1 == k:
            print(root.data, end=" ")
            return k
        else:
            printNodeFromKDistrance(root.left, k - right_distance - 2)
            return right_distance + 1
    elif left_distance + 1 == k:
        print(root.data, end=" ")
        return k
    else:
        printNodeFromKDistrance(root.right, k - left_distance - 2)
        return left_distance + 1


def nodesAtDistanceK(root, node, k):
    if not root:
        return
    
    printNodes(root, node, k)
