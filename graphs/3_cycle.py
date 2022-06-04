if __name__ == "__main__":
    N, E = list(map(int, input().split()))
    graph = dict()
    
    for i in range(N):
        graph[i] = set()
    
    for _ in range(E):
        node1, node2 = list(map(int, input().split()))
        
        graph[node1].add(node2)
        graph[node2].add(node1)

    count = 0
    
    for key1 in graph:
        for key2 in graph[key1]:
            for key3 in graph[key2]:
                if key1 in graph[key3]:
                    count += 1
    
    print(count // 6)
