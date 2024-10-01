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
    return [1,2]


def get_bfs_path():
    return [1,2]


def get_dijkstra_path():
    return [1,2]

def generate_random_path(graph, start, end):
    path = []
    path.append(start)
    
    curr_node = start

    while curr_node != end :
        neighbors = graph[curr_node][1]
        next_node = random.choice(neighbors)
        path.append(next_node)

    return path
