'''
Prim's algorithm for finding the Minimum Spanning Tree.
'''

import heapq


class Edge:
    '''
    Weighted edge between two vertices.
    '''
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight

    def __repr__(self):
        return f"{self.src} --{self.weight}--> {self.dest}"

class Prim:
    '''
    Builds MST.
    '''
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = {vertex: [] for vertex in vertices}

    def add_edge(self, src, dest, weight):
        '''
        Adds undirected edge.
        '''
        self.adj_list[src].append(Edge(src, dest, weight))
        self.adj_list[dest].append(Edge(dest, src, weight))

    def find_mst(self, start_vertex):
        '''
        Prim's algorithm.
        '''
        mst = []
        total_cost = 0
        visited = set()
        edge_heap = []

        visited.add(start_vertex)

        for edge in self.adj_list[start_vertex]:
            heapq.heappush(edge_heap, edge)

        while edge_heap and len(visited) < len(self.vertices):
            current_edge = heapq.heappop(edge_heap)

            if current_edge.dest in visited:
                continue

            visited.add(current_edge.dest)
            mst.append(current_edge)
            total_cost += current_edge.weight

            for next_edge in self.adj_list[current_edge.dest]:
                if next_edge.dest not in visited:
                    heapq.heappush(edge_heap, next_edge)

        return mst, total_cost


if __name__ == "__main__":
    vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    prim = Prim(vertices)

    prim.add_edge('A', 'B', 14)
    prim.add_edge('A', 'C', 6)
    prim.add_edge('A', 'E', 5)
    prim.add_edge('A', 'D', 10)
    prim.add_edge('B', 'D', 3)
    prim.add_edge('C', 'E', 4)
    prim.add_edge('D', 'F', 8)
    prim.add_edge('F', 'E', 2)
    prim.add_edge('E', 'G', 9)
    prim.add_edge('F', 'H', 15)

    mst_edges, min_cost = prim.find_mst('B') # starting point is B

    print("Edges in the Minimum Spanning Tree:")
    for edge in mst_edges:
        print(edge)

    print(f"\nTotal Cost of MST: {min_cost}")