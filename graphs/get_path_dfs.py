def print_path(graph, start, end, visited=set()):
    if start == end:
        print(end, end=" ")
        return True
    
    visited.add(start)
    
    for neighbour in graph[start]:
        if neighbour not in visited and print_path(graph, neighbour, end, visited):
            print(start, end=" ")
            return True
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
