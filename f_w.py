import math
import graph_data

def node_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def create_adjacency_matrix(graph):
    adj_matrix = [[float('inf')] * len(graph) for _ in range(len(graph))]
    
    for i in range(len(graph)):
        adj_matrix[i][i] = 0
    
    for i, (coord, neighbors) in enumerate(graph):
        for neighbor in neighbors:
            adj_matrix[i][neighbor] = node_distance(coord, graph[neighbor][0])
    
    return adj_matrix


def floyd_warshall(W):

    distance = [row[:] for row in W]
    parent = [[None if W[i][j] == float('inf') else i for j in range(len(distance))] for i in range(len(distance))]

    for k in range(len(W)):
        for i in range(len(W)):
            for j in range(len(W)):
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    parent[i][j] = parent[k][j]
    
    return parent

def reconstruct_path(parent, start, end):
    if parent[start][end] is None:
        return []
    
    path = []
    while end is not None:
        path.append(end)
        end = parent[start][end]
    
    return path[::-1]

graph = graph_data.graph_data[0]
adj_matrix = create_adjacency_matrix(graph)

result_matrix = floyd_warshall(adj_matrix)

print("\nShortest paths:")
for i in range(len(graph)):
    for j in range(len(graph)):
        if i != j:
            path = reconstruct_path(result_matrix, i, j)
            if path:
                print(f"Path from {i} to {j}: {path}")
            else:
                print(f"No path from {i} to {j}")