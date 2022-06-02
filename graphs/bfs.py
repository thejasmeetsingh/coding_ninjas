import queue


def BFS(graph):
    if not graph:
        return
    
    visited = set()
    
    for key in graph:
        if key not in visited:
            q = queue.Queue()
            q.put(key)
            
            while not q.empty():
                node = q.get()
                print(node, end=" ")
                
                for neighbour in sorted(graph[node]):
                    if neighbour not in visited:
                        visited.add(neighbour)
                        q.put(neighbour)
                        
                visited.add(node)
        
        

                
if __name__ == "__main__":
    N, E = list(map(int, input().split()))
    graph = dict()
    
    for i in range(N):
        graph[i] = []
    
    for _ in range(E):
        node1, node2 = list(map(int, input().split()))
        
        graph[node1].append(node2)
        graph[node2].append(node1)

    BFS(graph)
