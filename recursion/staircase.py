def staircase(n):
    if n <= 0:
        return 1 if n == 0 else 0
    
    x = staircase(n - 1)
    y = staircase(n - 2)
    z = staircase(n - 3)
    
    return x + y + z


if __name__ == "__main__":
    n = int(input())
    result = staircase(n)
    print(result)
