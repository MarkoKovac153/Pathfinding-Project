# Pathfinding-Project

##Brief
This is a simple pathfinding project I did using python in Jupiter notebook.
It allows for testing three different types of pathfinding on a grid of a chosen or random size.
One of the methods used is Dijkstra's algorithm. below is description and coding example of how it works
## Overview

Dijkstra's algorithm is a popular algorithm used to find the shortest paths between nodes in a graph. It works by iteratively selecting the node with the smallest distance from a source node and updating the distances of its neighbors accordingly. This process continues until all nodes have been visited or the destination node is reached. Dijkstra's algorithm is commonly used in various applications, such as network routing and pathfinding in games.

### Algorithm Steps:

1. **Initialization**: Assign a distance value to every node in the graph. Set the distance of the source node to 0 and all other nodes to infinity. Initialize an empty set to keep track of visited nodes and a priority queue (min heap) to store nodes ordered by their distances.

2. **Main Loop**: While there are unvisited nodes, repeat the following steps:
    - Select the node with the smallest distance from the priority queue.
    - Mark the selected node as visited.
    - Update the distances of its neighboring nodes if a shorter path is found.
    - Add neighboring nodes to the priority queue if they have not been visited.

3. **Termination**: The algorithm terminates when all nodes have been visited or the destination node is reached.

### Python Implementation:

```python
import heapq

def dijkstra(graph, source):
    distances = {node: float('infinity') for node in graph}
    distances[source] = 0
    visited = set()
    priority_queue = [(0, source)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node in visited:
            continue

        visited.add(current_node)

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Example usage:
graph = {
    'A': {'B': 5, 'C': 3},
    'B': {'A': 5, 'C': 2, 'D': 1},
    'C': {'A': 3, 'B': 2, 'D': 4, 'E': 6},
    'D': {'B': 1, 'C': 4, 'E': 7},
    'E': {'C': 6, 'D': 7}
}

source_node = 'A'
distances = dijkstra(graph, source_node)
print("Shortest distances from node", source_node + ":", distances)
