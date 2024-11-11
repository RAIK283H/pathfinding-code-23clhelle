import math

class Node:
    
    def __init__(self, graph, index):
        self.neighbors = graph[index][1]
        self.x, self.y = graph[index][0]
        self.index = index
        self.results = {}

        self.create_map(graph)
        

    def calculate_distance(self, graph, neighbor):
        start_coord = (self.x, self.y)
        end_coord = graph[neighbor][0]

        coords = zip(start_coord, end_coord)

        total = 0 
        for x, y in coords:
            total += (x - y)**2
        distance = math.sqrt(total)
        return distance
    
    def create_map(self, graph):
        for neighbor in self.neighbors:
            distance_to_neighbor = self.calculate_distance(graph, neighbor)
            self.results[neighbor] = distance_to_neighbor