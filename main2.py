import graph_data
import permutation

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

    return cycles

for graph_index in range(len(graph_data.graph_data) - 1):
    graph = graph_data.graph_data[graph_index]
    print("Graph Index: ", graph_index)
    cycles = check_for_hamiltonian(graph)
        
    if not cycles:
        print(-1)
    else:
        for perm in cycles:
            print(perm)
    
    print("")
