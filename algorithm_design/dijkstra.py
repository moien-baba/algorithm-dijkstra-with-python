### Algorithm Dijkstra ###
# this algorithm is for specify short path between two node in graph with min-heap

import heapq


N, M = map(int, input().split())


graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v, w = map(int, input().split())

    
    graph[u].append((v, w))
    graph[v].append((u, w))

start, target = map(int, input().split())


distance = [float('inf')] * (N + 1)
prev = [-1] * (N + 1)        # this list for determine the shortest path


priority_queue = []

distance[start] = 0
heapq.heappush(priority_queue, (0, start))

# shortest distance for each node
while priority_queue:

    current_distance, u = heapq.heappop(priority_queue)

   
    if current_distance > distance[u]:
        continue

    for v, w in graph[u]:

        new_dist = distance[u] + w

        if new_dist < distance[v]:

            distance[v] = new_dist
            prev[v] = u

            heapq.heappush(priority_queue, (new_dist, v))


if distance[target] == float('inf'):
    print("No path")

else:

    
    print(distance[target])

    print(prev)
    
    print(graph)

    path = []

    current = target

    while current != -1:
        path.append(current)
