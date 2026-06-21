'''
Dijkstra's algorithm to find the shortest path.
'''

import heapq


class Edge:
    '''
    Weighted edge between two vertices.
    '''
    def __init__(self, dest, weight):
        self.dest = dest
        self.weight = weight

class PathNode:
    '''
    Current shortest known distance from start vertex.
    '''
    def __init__(self, vertex, distance):
        self.vertex = vertex
        self.distance = distance

    def __lt__(self, other):
        return self.distance < other.distance

class Dijkstra:
    '''
    Finds shortest paths.
    '''
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = {vertex: [] for vertex in vertices}

    def add_edge(self, src, dest, weight):
        '''
        Adds directed edge.
        '''
        self.adj_list[src].append(Edge(dest, weight))

    def find_shortest_paths(self, start_vertex):
        '''
        Dijkstra's algorithm.
        '''
        distances = {vertex: float('inf') for vertex in self.vertices}
        previous_nodes = {vertex: None for vertex in self.vertices}
        
        distances[start_vertex] = 0
        
        heap = [PathNode(start_vertex, 0)]
        visited = set()

        while heap:
            current = heapq.heappop(heap)
            current_vertex = current.vertex
            current_distance = current.distance

            if current_vertex in visited:
                continue

            visited.add(current_vertex)

            for edge in self.adj_list[current_vertex]:
                neighbor = edge.dest
                
                if neighbor in visited:
                    continue

                new_distance = current_distance + edge.weight

                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous_nodes[neighbor] = current_vertex
                    
                    heapq.heappush(heap, PathNode(neighbor, new_distance))

        return distances, previous_nodes

    def reconstruct_path(self, previous_nodes, target_vertex):
        '''
        Rebuild from start to target.
        '''
        path = []
        current = target_vertex
        while current is not None:
            path.append(current)
            current = previous_nodes[current]
        
        return path[::-1]


if __name__ == "__main__":
    vertices = ['A', 'B', 'C', 'D', 'E']
    dijkstra = Dijkstra(vertices)

    dijkstra.add_edge('A', 'B', 4)
    dijkstra.add_edge('A', 'C', 1)
    dijkstra.add_edge('C', 'B', 2)
    dijkstra.add_edge('C', 'D', 4)
    dijkstra.add_edge('B', 'D', 1)
    dijkstra.add_edge('D', 'E', 3)

    start_node = 'A'
    
    shortest_distances, route_history = dijkstra.find_shortest_paths(start_node)

    print("Shortest distances from A:")
    for vertex in vertices:
        distance = shortest_distances[vertex]
        path = dijkstra.reconstruct_path(route_history, vertex)
        path_str = " -> ".join(path)
        print(f"To {vertex}: Cost = {distance} | Path = {path_str}")