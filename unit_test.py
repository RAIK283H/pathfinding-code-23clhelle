import math
import unittest
import pathing
import permutation
import main2


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
        assert(pathing.path_is_valid(graph, path))

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
            assert(perm in result, "{perm} was not in the resulting list")
        assert(len(permutations) == len(result), "the permutaion list lenghths are not equal")

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
        assert(len(permutations) == len(result), "the permutaion list lenghths are not equal")

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
            assert(perm in result, "{perm} was not in the list of hamiltonian cycles")
    
    def test_check_for_hamiltonian_false(self):
        graph = [
            [(0, 0), [1]],
            [(50, -200), [0, 2]],
            [(50, -300), [1, 3]],
            [(200, -500), [2]]
        ]
        result = main2.check_for_hamiltonian(graph)
        assert(result == -1, "there must have been a hamiltonian cycle found even though there wasn't supposed to be")

        


if __name__ == '__main__':
    unittest.main()