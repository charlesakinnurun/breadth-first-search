<h1 align="center">Breadth First Search</h1>

## Overview

**Breadth First Search (BFS)** is a graph traversal algorithm used to explore nodes level by level.
Instead of going deep into one branch like DFS, BFS visits all neighbors of a node first before moving to the next level.

BFS is widely used in:

* Shortest path in unweighted graphs
* Social network analysis
* Web crawling
* GPS navigation logic
* Broadcasting systems

<a href="/src/main.py">Check out for source code</a>

---

## 🧠 How BFS Works

BFS follows this process:

1. Start from a source node.
2. Visit the node and mark it as visited.
3. Add all its unvisited neighbors to a queue.
4. Remove the next node from the queue.
5. Repeat until the queue becomes empty.

👉 BFS always uses a **Queue (FIFO)** data structure.

---

## ⏱ Time and Space Complexity

| Case  | Complexity   |
| ----- | ------------ |
| Time  | **O(V + E)** |
| Space | **O(V)**     |

Where:

* **V** = number of vertices
* **E** = number of edges

---

## 🧩 BFS Example

### Graph Representation

```
A → B → D
↓
C → E
```

### BFS Traversal (starting from A)

```
A → B → C → D → E
```

Notice BFS explores nodes level by level.

---

## 💻 Python Implementation

### BFS Using Queue

```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

---

## 🧪 Sample Graph Input

```python
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}

bfs(graph, 'A')
# Output: A B C D E
```

---

## 🌍 Real-World Applications

* Finding shortest path in road maps
* Network broadcasting
* Friend suggestions in social media
* Crawling websites level by level
* Solving puzzles with minimum moves

---

## ✅ When to Use BFS

Use BFS when:

* You need the **shortest path in an unweighted graph**
* You want to explore nodes level by level
* You need minimum steps to reach a goal
* The graph is not extremely wide (to avoid high memory use)

---

## 📚 BFS vs DFS (Quick Comparison)

| Feature         | BFS                   | DFS               |
| --------------- | --------------------- | ----------------- |
| Data structure  | Queue                 | Stack / Recursion |
| Traversal style | Level-by-level        | Deep-first        |
| Shortest path   | ✅ Yes (unweighted)    | ❌ Not guaranteed  |
| Memory usage    | Higher on wide graphs | Lower             |

---

## 🏁 Summary

Breadth First Search is a fundamental graph traversal algorithm that explores nodes layer by layer using a queue. It is especially useful for shortest-path problems and level-order exploration tasks.

