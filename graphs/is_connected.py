if __name__ == "__main__":
    N, E = list(map(int, input().split()))
    graph = dict()
    
    for i in range(N):
        graph[i] = []
    
    for _ in range(E):
        node1, node2 = list(map(int, input().split()))
        
        graph[node1].append(node2)
        graph[node2].append(node1)
	
    keys = graph.keys()
    
    if len(keys) > 1:
        for key in keys:
            if not graph[key]:
                print("false")
                exit(0)
    
    print("true")
