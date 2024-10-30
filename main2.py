import graph_data
import permutation
import math

graph = graph_data.graph_data[0]

def is_hamiltonian_cycle(graph, path):
    # Check if the path starts and ends at the same node
    if path[0] != path[-1]:
        return False
    
    if len(path) < 4:
        return False
    
    # Check each consecutive node in the path to see if they are connected
    for i in range(len(path) - 1):
        node = path[i]
        next_node = path[i + 1]
        
        # Check if next_node is a neighbor of node
        if next_node not in graph[node][1]:
            return False
    
    return True

def check_for_hamiltonian(graph):
    all_permutations = permutation.determine_sjt(len(graph) - 1)
    cycles = []
    for perm in all_permutations:
        perm.remove(0)
        perm.append(1)
        if is_hamiltonian_cycle(graph, perm):
            perm.pop()
            if perm not in cycles:
                cycles.append(perm)

    if cycles:
        return cycles
    else:
        return -1
    
def shortest_cycle(cycles, graph):
    distance = float('inf')
    shortest_cycle = []
    for cycle in cycles:
        cycle_distance = 0
        for i in range(len(cycle) - 2):
            node_x = graph[i][0][0]
            node_y = graph[i][0][1]

            next_node_x = graph[i+1][0][0]
            next_node_y = graph[i+1][0][1]

            distance = math.sqrt(pow(node_x - next_node_x, 2) + pow(node_y - next_node_y, 2))
            cycle_distance = cycle_distance + distance
        if cycle_distance < distance:
            distance = cycle_distance
        shortest_cycle = cycles[i]
        
    
    return shortest_cycle


for graph_index in range(len(graph_data.graph_data) - 1):
    graph = graph_data.graph_data[graph_index]
    print("Graph Index: ", graph_index)
    cycles = check_for_hamiltonian(graph)
    
        
    if cycles == -1:
        print(-1)
    else:
        for perm in cycles:
            print(perm)
        
        #Extra Credit
        shortest = shortest_cycle(cycles, graph)
        print("Shortest Cycle: ", shortest)
    
    print("")
