def adjacency_list_to_matrix(adj_list, n):
    matrix = [[float('inf')] * n for _ in range(n)]
    
    for i in range(n):
        matrix[i][i] = 0
    
    for u, neighbors in adj_list.items():
        for v, weight in neighbors:
            matrix[u][v] = weight
    
    return matrix

def floyd_warshall(W):

    distance = [row[:] for row in W]

    for k in range(len()):
        for i in range(len()):
            for j in range(len()):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    return distance