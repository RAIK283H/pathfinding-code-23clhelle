import graph_data
import global_game_data
from numpy import random

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
    random_path_to_exit = generate_random_path(graph, global_game_data.target_node[graph_index], graph[len(graph) - 1][1])

    #if random_path_to_target is None :
     #   if random_path_to_exit is None : 
      #      print("ERROR")
       #     return []
        #else:
         #   return random_path_to_exit
    #elif(random_path_to_exit is None) : 
     #   return random_path_to_target

    #random_path = random_path_to_target[:-1] + random_path_to_exit   
    return random_path_to_target


def get_dfs_path():
    graph_index = int(global_game_data.current_graph_index)
    graph = graph_data.graph_data[graph_index]

    dfs_path_to_target = generate_dfs_path(graph, 0, global_game_data.target_node[graph_index])
    dfs_path_to_exit = generate_dfs_path(graph, global_game_data.target_node[graph_index], graph[len(graph) - 1])

    if dfs_path_to_target is None :
        if dfs_path_to_exit is None : 
            print("ERROR")
            return []
        else:
            return dfs_path_to_exit
    elif(dfs_path_to_exit is None) : 
        return dfs_path_to_target
    dfs_path = dfs_path_to_target[:-1] + dfs_path_to_exit
    return dfs_path


def get_bfs_path():
    return [1,2]


def get_dijkstra_path():
    return [1,2]

def generate_random_path(graph, start, end, path=[]):
    if start in path:
        print("error in random path, that node has already been visited")
        return None
    
    path = path + [start]

    if start == end:
        return path
    
    adj_list = graph[start][1]

    if adj_list is None:
        print('ERROR in random path, no neighbors found')
        return None


    random.shuffle(adj_list)
    for neighbor in adj_list:
        if neighbor not in path:
            new_path = generate_random_path(graph, neighbor, end, path)
            if new_path:
                return new_path
    return None
'''
    while adj_list:
        next_node = random.choice(adj_list)

        if next_node not in path:

            new_path = generate_random_path(graph, next_node, end, path)
            if new_path:
                return new_path
    return None
'''

def generate_dfs_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    for node in graph[start][1]:
        if node not in path:
            new_path = generate_dfs_path(graph, node, end, path)
            if new_path:
                return new_path
    return None