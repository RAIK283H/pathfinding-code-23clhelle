import unittest
import math
import pathing
import permutation
#import main2
import f_w


class TestPathFinding(unittest.TestCase):
    
    def test_upper(self):
        self.assertEqual('test'.upper(), 'TEST')

    def test_isupper(self):
        self.assertTrue('TEST'.isupper())
        self.assertFalse('Test'.isupper())

    def test_floating_point_estimation(self):
        first_value = 0
        for x in range(1000):
            first_value += 1/100
        second_value = 10
        almost_pi = 3.1
        pi = math.pi
        self.assertNotEqual(first_value,second_value)
        self.assertAlmostEqual(first=first_value,second=second_value,delta=1e-9)
        self.assertNotEqual(almost_pi, pi)
        self.assertAlmostEqual(first=almost_pi, second=pi, delta=1e-1)
    
    def test_path_is_valid(self):
        graph = [
            [(0, 0), [1]],
            [(200, -200), [0, 2]],
            [(200, -400), [1]]
            ]
        path = [1, 2]
        self.assertTrue(pathing.path_is_valid(graph, path), "path is not deemed valid")
    
    def test_determine_sjt(self):
        graph = [
            [(0, 0), [1]],
            [(200, -200), [0, 2]],
            [(200, -400), [1]]
            ]
        permutations = []
        permutations.append([0,1,2])
        permutations.append([0,2,1])
        permutations.append([1,0,2])
        permutations.append([1,2,0])
        permutations.append([2,1,0])
        permutations.append([2,0,1])
        result = permutation.determine_sjt(len(graph))
        for perm in permutations:
            assert perm in result, "{perm} was not in the resulting list"
        self.assertEqual(len(permutations), len(result), "the permutaion list lenghths are not equal") 

    def test_determine_sjt_length(self):
        graph = [
            [(0, 0), [1]],
            [(200, -200), [0, 2]],
            [(200, -400), [1]]
            ]
        permutations = []
        permutations.append([0,1,2])
        permutations.append([0,2,1])
        permutations.append([1,0,2])
        permutations.append([1,2,0])
        permutations.append([2,1,0])
        permutations.append([2,0,1])
        result = permutation.determine_sjt(len(graph))
        self.assertEqual(len(permutations), len(result), "the permutaion list lenghths are not equal")


    '''
    def test_check_for_hamiltonian(self):
        graph = [
            [(0, 0), [1]],
            [(50, -200), [0, 2, 3]],
            [(50, -300), [1, 3]],
            [(200, -500), [1, 2, 4]],
            [(300, -700), [3]]
        ]
        cycles = [[1,2,3], [1,3,2]]
        result = main2.check_for_hamiltonian(graph)
        for perm in cycles:
            self.assertIn(perm, result, "{perm} was not in the list of hamiltonian cycles")
    
    def test_check_for_hamiltonian_false(self):
        graph = [
            [(0, 0), [1]],
            [(50, -200), [0, 2]],
            [(50, -300), [1, 3]],
            [(200, -500), [2]]
        ]
        result = main2.check_for_hamiltonian(graph)
        self.assertEqual(result, -1, "there must have been a hamiltonian cycle found even though there wasn't supposed to be")
    '''   
    def test_node_distance_same(self):
        node1 = 200, 200
        node2 = 200, 200
        result = f_w.node_distance(node1, node2)
        self.assertEqual(result, 0, "node distance didn't work for the same node")

    def test_node_distance_different(self):
        node1 = 0, 0
        node2 = 200, 200
        result = f_w.node_distance(node1, node2)
        self.assertEqual(result, 282.842712474619, "distance did not work for two different nodes")
    
    def test_create_adj_matrix(self):
        graph = [
            [(0, 0), [1]],
            [(200, -200), [0, 2]],
            [(200, -400), [1]]
            ]
        result = f_w.create_adjacency_matrix(graph)
        expected = [
            [0, 282.842712474619, float('inf')], 
            [282.842712474619, 0, 200.0], 
            [float('inf'), 200.0, 0]
            ]
        self.assertEqual(result, expected, "the adjacency matrix was not created correctly")
        
    def test_floyd_warshall_parent(self):
        matrix = [[0, 282.842712474619, float('inf')], 
                  [282.842712474619, 0, 200.0], 
                  [float('inf'), 200.0, 0]]
        distance, result = f_w.floyd_warshall(matrix)
        expected = [[None, 0, 1], 
                    [1, None, 1], 
                    [1, 2, None]]
        self.assertEqual(result, expected, "floyd warshall did not return the correct parent matrix")

    def test_floyd_warshall_distance(self):
        matrix = [[0, 282.842712474619, float('inf')], 
                  [282.842712474619, 0, 200.0], 
                  [float('inf'), 200.0, 0]]
        distance, parent = f_w.floyd_warshall(matrix)
        expected = [[0, 282.842712474619, 482.842712474619], 
                    [282.842712474619, 0, 200.0], 
                    [482.842712474619, 200.0, 0]]
        self.assertEqual(distance, expected, "floyd warshall did not return the correct distance matrix")
if __name__ == '__main__':
    unittest.main()