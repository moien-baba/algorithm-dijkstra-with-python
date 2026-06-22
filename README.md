# Dijkstra's Shortest Path Algorithm

A Python implementation of Dijkstra's algorithm to find the shortest path in a weighted, undirected graph.

---

## Overview

This program uses **Dijkstra's algorithm** with a **Min-Heap (priority queue)** to compute the shortest distance between two specified nodes in a graph.

---

## Input Format

The program reads from standard input:

```
N M
u1 v1 w1
u2 v2 w2
...
start target
```

| Parameter | Description |
|-----------|-------------|
| `N` | Number of nodes |
| `M` | Number of edges |
| `u v w` | Edge between node `u` and node `v` with weight `w` |
| `start` | Source node |
| `target` | Destination node |

---

## Output

- If a path exists: prints the **shortest distance** between `start` and `target`.
- If no path exists: prints `No path`.

---

## Example

**Input:**
```
5 6
1 2 2
1 3 4
2 3 1
2 4 7
3 5 3
4 5 1
1 5
```

**Output:**
```
6
```

Shortest path: `1 → 2 → 3 → 5` with total distance 6

---

## Code Structure

```
graph[]          ← Adjacency list representation of the graph
distance[]       ← Shortest distance from source to each node
prev[]           ← Parent array for path reconstruction
priority_queue   ← Min-Heap for selecting the node with lowest distance
```

---

## Complexity

| Type | Complexity |
|------|------------|
| Time | `O((N + M) log N)` |
| Space | `O(N + M)` |

---

## Important Notes

- The graph is **undirected** and **weighted** (weights must be non-negative).
- The `prev` array is maintained for path reconstruction, but the path-rebuilding loop at the end of the code is **incomplete** and needs to be fixed:

```python
# Complete the path reconstruction loop:
while current != -1:
    path.append(current)
    current = prev[current]   # ← this line is missing
path.reverse()
print("Path:", path)
```

Without this fix, the loop runs **infinitely** since `current` is never updated.

---

## Dependencies

Only Python's standard library is used:

```python
import heapq
```

No external packages required.

---

## Usage

```bash
python dijkstra.py < input.txt
```
