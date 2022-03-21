def isBalanced(expression):
    if not expression:
        return True
    
    stack = []
    
    for char in expression:
        if char == '(':
            stack.append(char)
        else:
            if stack and '(' == stack[-1]:
                stack.pop()
    
    return True if not stack else False
