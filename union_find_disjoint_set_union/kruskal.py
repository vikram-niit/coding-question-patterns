class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        if self.rank[xr] < self.rank[yr]:
            self.parent[xr] = yr
        elif self.rank[xr] > self.rank[yr]:
            self.parent[yr] = xr
        else:
            self.parent[yr] = xr
            self.rank[xr] += 1
        return True

def kruskal(n, edges):
    """
    Kruskal's Algorithm to find the Minimum Spanning Tree (MST)
    :param n: number of nodes (0-indexed)
    :param edges: list of edges in form [weight, u, v]
    :return: total weight of MST and list of edges in MST
    """
    edges.sort()  # Sort edges by weight
    dsu = DSU(n)
    mst_weight = 0
    mst_edges = []

    for weight, u, v in edges:
        if dsu.union(u, v):
            mst_weight += weight
            mst_edges.append([u, v, weight])

    return mst_weight, mst_edges

# Example usage
if __name__ == "__main__":
    n = 4
    edges = [
        [1, 0, 1],
        [3, 0, 2],
        [2, 1, 2],
        [4, 1, 3],
        [5, 2, 3]
    ]
    weight, mst = kruskal(n, edges)
    print(f"MST weight: {weight}")
    print("Edges in MST:", mst)
