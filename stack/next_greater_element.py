if __name__ == "__main__":
    arr = list(map(int, input().split()))
    n, arr = arr[0], arr[1:]
    stack = list()
    result = []

    for i in range(n - 1, -1, -1):
        if stack:
            if stack[-1] > arr[i]:
                result.append(stack[-1])
            else:
                is_found = False

                while stack:
                    if stack[-1] > arr[i]:
                        is_found = True
                        break
                    stack.pop()

                if is_found:
                    result.append(stack[-1])
                else:
                    result.append(-1)
        else:
            result.append(-1)

        stack.append(arr[i])
    
    print(' '.join(map(str, result[::-1])))
