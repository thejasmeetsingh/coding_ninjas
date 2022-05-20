def get_staircase_count(n, hmap={}):
    a, b, c = 1, 2, 4
    
    if n == 0 or n == 1 or n == 2:
        return n
    
    if n == 3:
        return c
    
    d = 0
    
    for _ in range(4, n + 1):
        d = a + b + c
        a = b
        b = c
        c = d
    
    return d % 1000000007


if __name__ == "__main__":
    T = int(input())
    
    for _ in range(T):
        n = int(input())
        print(get_staircase_count(n))
