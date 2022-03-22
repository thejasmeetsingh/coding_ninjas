def countBracketReversals(inputString):
    if not inputString or len(inputString) % 2 != 0:
        return -1
    
    stack = list()
    
    for char in inputString:
        if char == '{':
            stack.append(char)
        elif char == '}':
            if not stack or stack[-1] == '}':
                stack.append(char)
            elif stack[-1] == '{':
                stack.pop()
        
    count = 0
    while stack:
        char1 = stack.pop()
        char2 = stack.pop()
        count += (1 if char1 == char2 else 2)
    
    return count
