# Kruskal's Algorithm - Minimum Spanning Tree (MST)

This repository contains a Python implementation of **Kruskal's Algorithm**, a classic algorithm to find the **Minimum Spanning Tree (MST)** of a weighted, undirected graph.

## Features

- Efficient **Disjoint Set Union (DSU)** implementation with path compression and union by rank.
- Returns both:
  - **Total weight of MST**
  - **Edges included in MST**
- Simple and easy to understand.

## Usage

```bash
python kruskal_mst.py
```

## Example

Input graph (edges as [weight, u, v]):

```
edges = [
    [1, 0, 1],
    [3, 0, 2],
    [2, 1, 2],
    [4, 1, 3],
    [5, 2, 3]
]
```

## Output:

```
MST weight: 7
Edges in MST: [[0, 1, 1], [1, 2, 2], [1, 3, 4]]
```

## How it works

Sort all edges by weight.

Use DSU to check if adding an edge forms a cycle.

Add edge to MST if it does not form a cycle.

Repeat until MST contains n-1 edges.
