class Edge:
    def __init__(self, src, dst, weight):
        self.src = src
        self.dst = dst
        self.weight = weight
        

if __name__ == "__main__":
    N, E = list(map(int, input().split()))
    edges = []
    parent = [i for i in range(N)]
    count = 0
    mst = []
    
    for _ in range(E):
        src, dst, weight = list(map(int, input().split()))
        edges.append(Edge(src, dst, weight))
    
    edges.sort(key=lambda x: x.weight)
    idx = 0
    
    for edge in edges:
        if count >= N - 1:
            break

        p1, p2 = edge.src, edge.dst

        while p1 != parent[p1]:
            p1 = parent[p1]

        while p2 != parent[p2]:
            p2 = parent[p2]

        if p1 != p2:
            mst.append(edge)
            parent[p1] = p2
            count += 1
	
    
    for _mst in mst:
        if _mst.src < _mst.dst:
            print(_mst.src, _mst.dst, _mst.weight)
        else:
            print(_mst.dst, _mst.src, _mst.weight)
