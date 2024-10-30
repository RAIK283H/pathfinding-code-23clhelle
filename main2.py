import graph_data
import permutation

graph = graph_data.graph_data[0]

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
            if next_node not in neighbors:
                return False  # No edge between consecutive nodes

    return True

for graph_index in range(len(graph_data.graph_data) - 1):
    graph = graph_data.graph_data[graph_index]
    print("Graph Index: ", graph_index)

    permutations = permutation.determine_sjt(len(graph))

    no_perms = True
    for perm in permutations:

        # Check for hamiltonian cycle
        path = list(perm) + [perm[0]]  # Close the loop by appending the first node
        print(path)

        if is_hamiltonian_cycle(graph, path):
            print(f"Hamiltonian Cycle found: {path}")
            break

            
        str_perm = ''.join(str(num) for num in perm)
        first = str_perm[0]
        last = str_perm[-1]
        
        if first == str(1) and last == str(len(graph)):
            no_perms = False
            print(str_perm)
        
    if no_perms:
        print(-1)
    
    print("")