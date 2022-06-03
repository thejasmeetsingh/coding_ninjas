import queue


def has_path(graph, start, end):
    if not graph:
        return False
    
    visited = set()
    q = queue.Queue()
    q.put(start)

    while not q.empty():
        node = q.get()
        
        if node == end:
            return True

        for neighbour in sorted(graph[node]):
            if neighbour not in visited:
                visited.add(neighbour)
                q.put(neighbour)

        visited.add(node)
    
    return False

                
if __name__ == "__main__":
    N, E = list(map(int, input().split()))
    graph = dict()
    
    for i in range(N):
        graph[i] = set()
    
    for _ in range(E):
        node1, node2 = list(map(int, input().split()))
        
        graph[node1].add(node2)
        graph[node2].add(node1)
	
    start, end = list(map(int, input().split()))
    print("true" if has_path(graph, start, end) else "false")
