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
    return [1,2]


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