def reverseStack(inputStack, extraStack) :
    while inputStack:
        extraStack.append(inputStack.pop())
    
    while extraStack:
        inputStack.append(extraStack.pop(0))
