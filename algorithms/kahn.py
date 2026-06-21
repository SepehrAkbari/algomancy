'''
Kahn's Algorithm for topological sorting.
'''

from collections import deque


class Edge:
    '''
    Directed edge between two vertices.
    '''
    def __init__(self, dest):
        self.dest = dest

    def __repr__(self):
        return f"-> {self.dest}"

class kahn:
    '''
    Sorts topologically.
    '''
    
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = {vertex: [] for vertex in vertices}
        self.in_degree = {vertex: 0 for vertex in vertices}

    def add_edge(self, src, dest):
        """Adds a directed dependency (src must come before dest)."""
        self.adj_list[src].append(Edge(dest))
        self.in_degree[dest] += 1

    def topological_sort(self):
        '''
        Kahn's algorithm.
        '''
        queue = deque([vertex for vertex in self.vertices if self.in_degree[vertex] == 0])
        
        topological_order = []

        while queue:
            current_vertex = queue.popleft()
            topological_order.append(current_vertex)

            for edge in self.adj_list[current_vertex]:
                neighbor = edge.dest
                self.in_degree[neighbor] -= 1

                if self.in_degree[neighbor] == 0:
                    queue.append(neighbor)

        if len(topological_order) != len(self.vertices):
            raise ValueError("Error: The graph contains a cycle. A valid topological sort is impossible.")

        return topological_order


if __name__ == "__main__":
    vertices = ['A', 'B', 'C', 'D', 'E', 'F']
    kahn = kahn(vertices)

    kahn.add_edge('A', 'C')
    kahn.add_edge('B', 'C')
    kahn.add_edge('B', 'D')
    kahn.add_edge('C', 'E')
    kahn.add_edge('E', 'F')
    kahn.add_edge('D', 'F')
    
    try:
        execution_order = kahn.topological_sort()
        print("Valid Execution Order:")
        for priority, vertex in enumerate(execution_order, 1):
            print(f"Priority {priority}: {vertex}")
    except ValueError as e:
        print(e)