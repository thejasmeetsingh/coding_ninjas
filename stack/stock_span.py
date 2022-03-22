def stockSpan(price, n):
    if not price:
        return []
    
    result = [1]
    stack = [0]
    
    for i in range(1, n):
        if price[i] < price[stack[-1]]:
            stack.append(i)
            result.append(1)
        else:
            while stack and price[i] > price[stack[-1]]:
                stack.pop()
            
            result.append(i + 1 if not stack else i - stack[-1])
            stack.append(i)
    
    return result
