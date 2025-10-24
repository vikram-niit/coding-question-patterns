# Depth-First Search (DFS) Graph Traversal
A simple Python implementation of **DFS** for graphs using an adjacency list.

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
