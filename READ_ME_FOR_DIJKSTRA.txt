DIJKSTRA ALGORITHM - README

Objective:
To find the shortest path between cities using Dijkstra Algorithm.

Description:
Dijkstra Algorithm is a greedy algorithm used to find the minimum distance
from a source node to all other nodes in a weighted graph.

Steps:
1. Initialize distance of source = 0 and others = infinity
2. Use priority queue (min heap)
3. Pick the node with minimum distance
4. Update distances of neighbors
5. Repeat until all nodes are visited

Input:
- CSV file containing Source, Destination and Distance

Output:
- Shortest distance from source to all cities

Applications:
- Google Maps
- Network Routing
- AI Pathfinding

Conclusion:
Dijkstra guarantees shortest path in graphs with non-negative weights.
