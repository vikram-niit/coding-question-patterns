# 🎒 Depth-First Search (DFS) Graph Traversal
A simple Python implementation of **DFS** for graphs using an adjacency list.

📘 **Problem**

Given a **graph** (directed or undirected), perform **Depth-First Search (DFS)** starting from a given node.  
DFS visits nodes as far as possible along each branch before backtracking.


⚙️ **Approach**

Use a **recursive DFS strategy**:
1. Maintain a `visited` set to track visited nodes.
2. Visit the start node and mark it as visited.
3. Recursively visit all unvisited neighbors.

**Transition / Formula**
```
visited.add(node)
for neighbor in graph[node]:
    if neighbor not in visited:
        dfs_util(neighbor, visited)
```

**Code (Python)**
```python
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs_util(self, node, visited):
        visited.add(node)
        print(node, end=" ")
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                self.dfs_util(neighbor, visited)

    def dfs(self, start_node):
        visited = set()
        print("DFS traversal starting from node", start_node, ":")
        self.dfs_util(start_node, visited)

# Example usage
if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    g.dfs(2)

```

## Features
- DFS traversal from a start node
- Supports directed graphs
- Prints nodes in visited order

## Usage
1. Clone the repo:
    ```bash
    git clone <repo-url>
    cd <repo-folder>
    ```
2. Run the script:
    ```bash
    python dfs_graph.py
    ```

## Example
Edges:
0 -> 1 
0 -> 2 
1 -> 2 
2 -> 0 
2 -> 3 
3 -> 3 

DFS starting from node 2 outputs:
2 0 1 3

## Complexity

Time: O(V + E) (V = number of vertices, E = number of edges)

Space: O(V) (for the visited set + recursion stack)

## 🧠 Key Insight
DFS explores deep paths first, making it useful for:

Connected components

Cycle detection

Topological sorting

Maze or grid traversal
