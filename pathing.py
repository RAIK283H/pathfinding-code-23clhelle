import graph_data
import global_game_data
from numpy import random
from collections import deque


def set_current_graph_paths():
    global_game_data.graph_paths.clear()
    global_game_data.graph_paths.append(get_test_path())
    global_game_data.graph_paths.append(get_random_path())
    global_game_data.graph_paths.append(get_dfs_path())
    global_game_data.graph_paths.append(get_bfs_path())
    global_game_data.graph_paths.append(get_dijkstra_path())


def get_test_path():
    return graph_data.test_path[global_game_data.current_graph_index]


def get_random_path():
    
    graph_index = int(global_game_data.current_graph_index)
    graph = graph_data.graph_data[graph_index]

    
    random_path_to_target = generate_random_path(graph, 0, global_game_data.target_node[graph_index])
    random_path_to_exit = generate_random_path(graph, global_game_data.target_node[graph_index], len(graph) - 1)

    random_path = random_path_to_target[:-1] + random_path_to_exit
    assert(path_is_valid(graph, random_path))   
    
    return random_path
    


def get_dfs_path():
    graph_index = int(global_game_data.current_graph_index)
    graph = graph_data.graph_data[graph_index]
    target = global_game_data.target_node[graph_index]

    visited = [False] * len(graph)
    
    dfs_path_to_target = generate_dfs_path(graph, 0, target, visited)

    dfs_path_to_end = generate_dfs_path(graph, target, len(graph) - 1, visited)

    dfs_path = dfs_path_to_target + dfs_path_to_end[1:]

    assert(target in dfs_path, "path doesn't hit target")
    assert(dfs_path[-1] == len(graph) - 1, "path doesn't stop at end")

    '''
    for i in range(len(dfs_path) - 2):
        next = i + 1
        assert(next in graph[i][1])
    '''

    return dfs_path




def get_bfs_path():
    
    graph_index = int(global_game_data.current_graph_index)
    graph = graph_data.graph_data[graph_index]
    target = global_game_data.target_node[graph_index]
    
    bfs_path_to_target = generate_bfs_path(graph, 0, target)
    bfs_path_to_end = generate_bfs_path(graph, target, len(graph) - 1)

    bfs_path = bfs_path_to_target + bfs_path_to_end[1:]

    assert(target in bfs_path, "path doesn't hit target")
    assert(bfs_path[-1] == len(graph) - 1, "path doesn't stop at end")

    return bfs_path
    


def get_dijkstra_path():
    return [1,2]

def generate_random_path(graph, start, target):
    path = []
    if start != 0:
        path.append(start)
    curr_node = start

    while curr_node != target :
        neighbors = list(graph[curr_node][1])
        
        valid_neighbors = neighbors[:]
        last_node_num = len(graph) - 1
        
       
        # remove the exit node from neighbors if trying to get to target
        if (last_node_num in valid_neighbors) and (last_node_num != target):
            valid_neighbors.remove(last_node_num)

        # remove beginning if start is target
        if 0 in valid_neighbors :
            valid_neighbors.remove(0)

        # remove visited nodes from neighbors
        for node in path:
            if node in valid_neighbors:
                valid_neighbors.remove(node)
        
        # No valid neighbors, the path is stuck
        if not valid_neighbors: 
            # allow it to backtrack
            valid_neighbors = neighbors[:]
            '''
            if len(valid_neighbors) != 1:
                if (last_node_num in valid_neighbors) and (last_node_num != target):
                    valid_neighbors.remove(last_node_num)
                if 0 in valid_neighbors :
                    valid_neighbors.remove(0)
                if start in valid_neighbors:
                    valid_neighbors.remove(start)
                    '''
            
        # randomly choose a neighbor
        next_node = int(random.choice(valid_neighbors))
        path.append(next_node)
        curr_node = path[-1]
    return path


def generate_dfs_path(graph, start, target, visited):
    
    s = [(start)]
    path = [(start)]

    while s:
        u = s.pop()
        
        # if reached the target, return the path
        if u == target:
            print("SUCCESS")
            path.append(u)
            if 0 in path:
                path.remove(0)
            return path
        
        if not visited[u]:
            visited[u] = True
            
            if u not in path:
                path.append(u)

            neighbors = graph[u][1]
            for neighbor in neighbors:
                if not visited[neighbor]:
                    s.append(neighbor)
                    break
        #else:
            # Backtracking
            #path.pop()

    return path



def generate_bfs_path(graph, start, target):
    visited = [False] * len(graph) 
    q = deque([(start, [start])])

    while q:
        u, path = q.popleft() 
        
        # If reached the target, return the path
        if u == target:
            if 0 in path:
                path.remove(0)
            return path
        
       
        if not visited[u]:
            visited[u] = True
            
            # Explore all neighbors of the current node
            neighbors = graph[u][1]
            for neighbor in neighbors:
                if not visited[neighbor]:
                    q.append((neighbor, path + [neighbor]))

    return []

    


def path_is_valid(graph, path):
    for i in range(len(path) - 1):
        if path[i+1] not in graph[path[i]][1]: #check each node of path
            return False
        
    return True