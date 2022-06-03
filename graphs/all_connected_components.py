import sys
sys.setrecursionlimit(10 ** 6)



def dfs_traversal(graph, node, visited, result):
    visited.add(node)
    result.append(node)
    
    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs_traversal(graph, neighbour, visited, result)


def DFS(graph):
    visited = set()
    
    for key in graph:
        if key not in visited:
            result = []
            dfs_traversal(graph, key, visited, result)
            result.sort()
            print(' '.join(map(str, result)))
            print()


if __name__ == "__main__":
    N, E = list(map(int, input().split()))
    graph = dict()
    
    for i in range(N):
        graph[i] = []
    
    for _ in range(E):
        node1, node2 = list(map(int, input().split()))
        
        graph[node1].append(node2)
        graph[node2].append(node1)

    DFS(graph)
