import graph_data
import permutation

graph = graph_data.graph_data[0]

permutations = permutation.determine_sjt(len(graph))

for perm in permutations:
    str_perm = ''.join(str(num) for num in perm)
    print(str_perm)