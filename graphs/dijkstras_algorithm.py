import sys


def get_min_vertex(visited, distance, N):
    min_vertex = -1
    
    for i in range(N):
        if i not in visited and (min_vertex == -1 or distance[i] < distance[min_vertex]):
            min_vertex = i
    
    return min_vertex


if __name__ == "__main__":
    N, E = list(map(int, input().split()))
    graph = [[0 for __ in range(N)] for _ in range(N)]
    
    for _ in range(E):
        v1, v2, weight = list(map(int, input().split()))
        graph[v1][v2] = weight
        graph[v2][v1] = weight
    
    visited = set()
    distance = [sys.maxsize for _ in range(N)]
    distance[0] = 0
    
    for i in range(N - 1):
        min_vertex = get_min_vertex(visited, distance, N)
        visited.add(min_vertex)
        
        for j in range(N):
            if j not in visited and graph[min_vertex][j] != 0:
                distance[j] = min(distance[j], distance[min_vertex] + graph[min_vertex][j])
    
    for i in range(N):
        print(i, distance[i])
