'''
Kruskal's Algorithm for finding the Minimum Spanning Tree.
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

class DisjointSet:
    '''
    Disjoint Set (Union-Find) data structure.
    '''
    def __init__(self, vertices):
        self.parent = {vertex: vertex for vertex in vertices}
        self.rank = {vertex: 0 for vertex in vertices}

    def find(self, vertex):
        '''
        Finds root of set containing vertex.
        '''
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, vertex1, vertex2):
        '''
        Unites two sets. False if already in the same set, True otherwise.
        '''
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)

        if root1 == root2:
            return False

        # union by rank
        if self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        elif self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        else:
            self.parent[root2] = root1
            self.rank[root1] += 1
            
        return True

class Kruskal:
    '''
    Builds MST.
    '''
    def __init__(self, vertices):
        self.vertices = vertices
        self.edge_heap = []

    def add_edge(self, src, dest, weight):
        '''
        Adds edge to min-heap based on weight.
        '''
        edge = Edge(src, dest, weight)
        heapq.heappush(self.edge_heap, edge)

    def find_mst(self):
        '''
        Kruskal's algorithm.
        '''
        mst = []
        total_cost = 0
        disjoint_set = DisjointSet(self.vertices)

        while self.edge_heap and len(mst) < len(self.vertices) - 1:
            current_edge = heapq.heappop(self.edge_heap)

            if disjoint_set.union(current_edge.src, current_edge.dest):
                mst.append(current_edge)
                total_cost += current_edge.weight

        return mst, total_cost


if __name__ == "__main__":
    vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    kruskal = Kruskal(vertices)

    kruskal.add_edge('A', 'B', 2)
    kruskal.add_edge('A', 'G', 8)
    kruskal.add_edge('A', 'F', 14)
    kruskal.add_edge('G', 'F', 21)
    kruskal.add_edge('B', 'F', 25)
    kruskal.add_edge('B', 'C', 19)
    kruskal.add_edge('F', 'C', 17)
    kruskal.add_edge('F', 'E', 13)
    kruskal.add_edge('C', 'E', 5)
    kruskal.add_edge('E', 'D', 1)
    kruskal.add_edge('C', 'D', 9)

    mst_edges, min_cost = kruskal.find_mst()

    print("Edges in the Minimum Spanning Tree:")
    for edge in mst_edges:
        print(edge)

    print(f"\nTotal Cost of MST: {min_cost}")