def checkRedundantBrackets(expression):
    if not expression:
        return False
    
    stack, count, i, length = list(), 0, 0, len(expression)
    
    while i < length:
        while expression[i] != ')':
            if not expression[i]:
                return False
            
            stack.append(expression[i])
            i += 1
        
        if expression[i] == ')':
            if not stack:
                return False
            
            while stack and stack[-1] != '(':
                stack.pop()
                count += 1
            
            if count == 0 or count == 1:
                return True
            else:
                stack.pop()
                count = 0
        i += 1
    
    return False
