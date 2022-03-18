def printReverse(head):
    if not head:
        return
    
    printReverse(head.next)
    print(head.data, end=" ")
