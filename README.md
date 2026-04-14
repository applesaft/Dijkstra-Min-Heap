# Dijkstra-Min-Heap

This project implements **Dijkstra's algorithm** using a **Binary Min Heap**, all from scratch in Python. 
The program accepts a graph via the CLI, given in the form of an Adjacency Matrix, a source node and a destination node and outputs the shortest path between the two nodes.
 
Resources - Binary Heaps and Dijkstra's Algorithm,
**https://youtu.be/AE5I0xACpZs?si=i9AggxA3KeDYlunl**
**https://youtu.be/EFg3u_E6eHU?si=7_uFdMbmfjdQLwcP**

## Project structure
```
Dijkstra-Min-Heap/
├── dijkstra_min_heap/
│   ├── main.py           # entry point
│   ├── dijkstra.py       # shortest path algorithm
│   ├── min_heap.py       # pointer-based binary min-heap
│   ├── min_heap_node.py  # HeapNode class
│   └── cli.py            # user input and result display
├── README.md
```
Dependencies - `rich` — terminal formatting and tables
 
## Example
 
For a graph with 5 nodes, entering this adjacency matrix:
 
```
     0   1   2   3   4
0  [ 0,  2,  6,  0,  0 ]
1  [ 0,  0,  0,  3,  0 ]
2  [ 0,  0,  0,  1,  0 ]
3  [ 0,  0,  0,  0,  5 ]
4  [ 0,  0,  0,  0,  0 ]
```
 
Source `0`, destination `4` produces:
 
```
+-----+--------+--------+--------+-----------------+
| Hop |  From  |   To   | Weight | Cumulative Cost |
+-----+--------+--------+--------+-----------------+
|  1  | Node 0 | Node 1 |   2    |        2        |
|  2  | Node 1 | Node 3 |   3    |        5        |
|  3  | Node 3 | Node 4 |   5    |       10        |
+-----+--------+--------+--------+-----------------+
Total cost: 10
```