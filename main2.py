import graph_data
import permutation

graph = graph_data.graph_data[0]

'''
def is_hamiltonian_cycle(graph, path):
    # Check if the path forms a closed loop
    if path[0] != path[-1]:
        return False
    
    # Check if all nodes are visited exactly once
    visited = set(path[:-1])  # Exclude the last node which is the same as the first
    if len(visited) != len(graph):
        return False

    # Validate edges
    for i in range(len(path) - 1):
        node, next_node = path[i], path[i+1]

        if node is not len(graph):
            neighbors = graph[node][1]  # Get neighbors of the current node
            if next_node not in neighbors and next_node != len(graph):
                return False  # No edge between consecutive nodes

    return True
'''
def is_hamiltonian_cycle(graph, path):
    # Check if the path starts and ends at the same node
    if path[0] != path[-1]:
        return False
    
    if len(path) < 2:
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
    for perm in all_permutations:
        perm.remove(len(graph) - 1)
        perm.append(1)
        print(perm)
        if is_hamiltonian_cycle(graph, perm):
            print("Hamiltonian Cycle found:", perm)

for graph_index in range(len(graph_data.graph_data) - 1):
    graph = graph_data.graph_data[graph_index]
    print("Graph Index: ", graph_index)
    check_for_hamiltonian(graph)

    permutations = permutation.determine_sjt(len(graph))

    no_perms = True
    for perm in permutations:   
        str_perm = ''.join(str(num - 1) for num in perm)
        first = str_perm[0]
        last = str_perm[-1]
        
        if first == str(0) and last == str(len(graph) - 1):
            no_perms = False
            print(str_perm)
        
    if no_perms:
        print(-1)
    
    print("")
