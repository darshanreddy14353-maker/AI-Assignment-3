import csv
import heapq

def load_graph(filename):
    graph = {}

    with open(filename, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            u = row['Source']
            v = row['Destination']
            w = int(row['Distance'])

            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []

            graph[u].append((v, w))
            graph[v].append((u, w))

    return graph


def dijkstra(graph, start):
    pq = [(0, start)]
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


graph = load_graph("Cities.csv")

start = input("Enter starting city: ")
result = dijkstra(graph, start)

print("\nShortest distances:")
for city, dist in result.items():
    print(city, ":", dist)
