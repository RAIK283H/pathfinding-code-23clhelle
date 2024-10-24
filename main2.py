import graph_data
import permutation

graph = graph_data.graph_data[0]

for graph_index in range(len(graph_data.graph_data) - 1):
    graph = graph_data.graph_data[graph_index]
    print("Graph Index: ", graph_index)

    permutations = permutation.determine_sjt(len(graph))

    count = 0
    for perm in permutations:
        str_perm = ''.join(str(num) for num in perm)
        print(str_perm)
        count = count + 1
    
    print("")