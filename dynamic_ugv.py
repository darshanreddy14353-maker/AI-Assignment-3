import heapq
import random

GRID_SIZE = int(input("Enter grid size: "))

start = (0, 0)
goal = (GRID_SIZE-1, GRID_SIZE-1)

grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

for i in range(GRID_SIZE):
    for j in range(GRID_SIZE):
        if random.random() < 0.2:
            grid[i][j] = 1

def neighbors(node):
    x, y = node
    moves = [(1,0), (-1,0), (0,1), (0,-1)]
    result = []

    for dx, dy in moves:
        nx, ny = x+dx, y+dy
        if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:
            if grid[nx][ny] == 0:
                result.append((nx, ny))

    return result


def dijkstra_grid(start, goal):
    pq = [(0, start)]
    visited = set()

    while pq:
        cost, node = heapq.heappop(pq)

        if node == goal:
            print("Reached goal with cost:", cost)
            return

        if node in visited:
            continue

        visited.add(node)

        for n in neighbors(node):
            heapq.heappush(pq, (cost+1, n))

    print("No path found")


dijkstra_grid(start, goal)
