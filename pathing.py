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

    for i in dfs_path_to_target:
        visited[i] = True
    visited[target] = False


    dfs_path_to_end = generate_dfs_path(graph, target, len(graph) - 1, visited)

    dfs_path = dfs_path_to_target + dfs_path_to_end[1:]

    assert(target in dfs_path)
    assert(dfs_path[-1] == len(graph) - 1)

    return dfs_path

'''
    for i in range(len(dfs_path) - 2):
        next = i + 1
        assert(next in graph[i][1])

    return dfs_path
    '''
    #return [1,2]



def get_bfs_path():
    '''
    graph_index = int(global_game_data.current_graph_index)
    graph = graph_data.graph_data[graph_index]
    target = global_game_data.target_node[graph_index]
    
    bfs_path_to_target = generate_bfs_path(graph, 0, target)
    bfs_path_to_end = generate_bfs_path(graph, target, len(graph) - 1)

    bfs_path = bfs_path_to_target + bfs_path_to_end[1:]
    return bfs_path
    '''
    return [1,2]


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

'''
def generate_dfs_path(graph, start, target):
    print("CALLED GENERATE")
    visited = [False] * (len(graph))
    s = []
    path = []
    visited[start] = True
    s.append(start)
    while s:
        u = s[-1]
        path.append(u)
        s.remove(u)

        if u == target:
            path.remove(start)
            return path
        
        neighbors =  graph[u][1]
        for neighbor in neighbors:
            if visited[neighbor] == False:
                s.append(u)
                visited[neighbor] = True
                s.append(neighbor)

'''
def generate_dfs_path(graph, start, target, visited):
    s = [start]  # Stack for DFS
    path = []    # Store the path taken

    while s:
        u = s.pop()

        # If we have reached the target, return the path
        if u == target:
            path.append(u)  # Add the target to the path
            return path  # Return the full path when the target is found

        if not visited[u]:
            visited[u] = True  # Mark the node as visited
            path.append(u)  # Add to the current path

            # Check all neighbors of the current node
            neighbors = graph[u][1]
            for neighbor in neighbors:
                if not visited[neighbor]:
                    s.append(neighbor)  # Only add unvisited neighbors to the stack
                    break  # Explore only one neighbor at a time
        else:
            # Backtrack by removing the last node added to the path
            path.pop()

    print("No path found from", start, "to", target)
    return []  # Return an empty list if no path is found





'''    
def generate_dfs_path(graph, start, target, visited):
    path = []
    
    # Recursive DFS helper
    def dfs(node):
        # Add the current node to the path
        path.append(node)
        print(f"Visiting node {node}, current path: {path}")
        
        # If we reached the target, return True to indicate success
        if node == target:
            print(f"Target {target} found!")
            return True
        
        # Mark the current node as visited
        visited[node] = True
        
        # Explore all neighbors of the current node
        for neighbor in graph[node][1]:
            if not visited[neighbor]:
                print(f"Exploring neighbor {neighbor} of node {node}")
                # Recursively call DFS on the neighbor
                if dfs(neighbor):
                    return True  # If target is found, unwind and stop searching
        
        # If no valid path was found from this node, backtrack
        print(f"Backtracking from node {node}, current path: {path}")
        if node == target:
            return True
        path.pop()  # Remove the node from the path as we backtrack
        return False
    
    # Start DFS from the start node
    if dfs(start):
        return path
    else:
        # If no path is found, return an empty list
        print(f"No valid path found from {start} to {target}")
        return []
'''
'''
def generate_dfs_path(graph, start, target, visited):
    
    s = [(start)]
    path = [(start)]

    while s:
        u = s.pop()
        
        # if reached the target, return the path
        if u == target:
            path.append(u)
            print(f"Target {target} found!")
            return path
        
        if not visited[u]:
            visited[u] = True

            neighbors = graph[u][1]
            for neighbor in neighbors:
                if not visited[neighbor]:
                    s.append(neighbor)
                    path.append(neighbor)
                    break
        else:
            # Backtracking
            path.pop()

    return path
'''


def generate_bfs_path(graph, start, target):
    visited = [False] * len(graph)
    
    Q = [(start, [start])]

    while(Q is not []):
        u, curr_path = Q.pop(0)

        # if reached the target, return the path
        if u == target:
            return curr_path

        for neighbor in graph[u][1]:
            if visited[neighbor] == False:
                visited[neighbor] = True
                Q.append((neighbor, curr_path + [neighbor]))
    return[1]
    


def path_is_valid(graph, path):
    for i in range(len(path) - 1):
        if path[i+1] not in graph[path[i]][1]: #check each node of path
            return False
        
    return True