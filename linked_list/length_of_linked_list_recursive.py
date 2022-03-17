def lengthRecursive(head):
    if not head:
        return 0
    return 1 + lengthRecursive(head.next)
