import queue


def print_path(graph, start, end):
    if not graph:
        return []
    
    visited = set()
    q = queue.Queue()
    result = []
    hmap = {}
    
    q.put(start)

    while not q.empty():
        node = q.get()

        for neighbour in graph[node]:
            if neighbour not in visited:
                
                visited.add(neighbour)
                q.put(neighbour)
                hmap[neighbour] = node
                
                if neighbour == end:
                    print(end, end=" ")
                    
                    while end != start:
                        end = hmap[end]
                        print(end, end=" ")
                    
                    return

                
if __name__ == "__main__":
    N, E = list(map(int, input().split()))
    graph = dict()
    
    for i in range(N):
        graph[i] = []
    
    for _ in range(E):
        node1, node2 = list(map(int, input().split()))
        
        graph[node1].append(node2)
        graph[node2].append(node1)
	

    start, end = list(map(int, input().split()))
    print_path(graph, start, end)
