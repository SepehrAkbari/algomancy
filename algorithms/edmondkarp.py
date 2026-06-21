'''
Edmond-Karp algorithm for maximizing network flow.
'''

from collections import deque


class FlowEdge:
    '''
    Directed edge with capacity and current flow between two vertices.
    '''
    def __init__(self, src, dest, capacity):
        self.src = src
        self.dest = dest
        self.capacity = capacity
        self.flow = 0
        # pointer to reverse edge in residuals
        self.reverse_edge = None 

    @property
    def residual_capacity(self):
        '''
        Available capacity in residual graph.
        '''
        return self.capacity - self.flow

    def __repr__(self):
        return f"{self.src} -> {self.dest} (Flow: {self.flow}/{self.capacity})"

class NetworkFlowAlgorithm:
    '''
    Computes maximum flow.
    '''
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = {vertex: [] for vertex in vertices}

    def add_edge(self, src, dest, capacity):
        '''
        Adds directed edge with capacity.
        '''
        forward_edge = FlowEdge(src, dest, capacity)
        
        reverse_edge = FlowEdge(dest, src, 0)
        
        forward_edge.reverse_edge = reverse_edge
        reverse_edge.reverse_edge = forward_edge
        
        self.adj_list[src].append(forward_edge)
        self.adj_list[dest].append(reverse_edge)

    def _bfs_find_path(self, source, sink):
        '''
        BFS to find augmenting path in residual graph.
        '''
        parent_edge = {vertex: None for vertex in self.vertices}
        queue = deque([source])
        visited = {source}

        while queue:
            current = queue.popleft()

            if current == sink:
                break

            for edge in self.adj_list[current]:
                if edge.residual_capacity > 0 and edge.dest not in visited:
                    visited.add(edge.dest)
                    parent_edge[edge.dest] = edge
                    queue.append(edge.dest)

        return parent_edge

    def maximize_flow(self, source, sink):
        '''
        Maximum flow from source to sink.
        '''
        max_total_flow = 0

        while True:
            parent_edge = self._bfs_find_path(source, sink)

            if parent_edge[sink] is None:
                break

            push_flow = float('inf')
            current = sink
            while current != source:
                edge = parent_edge[current]
                push_flow = min(push_flow, edge.residual_capacity)
                current = edge.src

            current = sink
            while current != source:
                edge = parent_edge[current]
                
                edge.flow += push_flow
                
                edge.reverse_edge.flow -= push_flow
                
                current = edge.src

            max_total_flow += push_flow

        return max_total_flow


if __name__ == "__main__":
    # s = source, t = sink
    vertices = ['s', 'A', 'B', 'C', 'D', 't']
    flow_network = NetworkFlowAlgorithm(vertices)

    flow_network.add_edge('s', 'A', 10)
    flow_network.add_edge('s', 'B', 10)
    flow_network.add_edge('A', 'B', 2)
    flow_network.add_edge('A', 'C', 4)
    flow_network.add_edge('A', 'D', 8)
    flow_network.add_edge('B', 'D', 9)
    flow_network.add_edge('C', 't', 10)
    flow_network.add_edge('D', 'C', 6)
    flow_network.add_edge('D', 't', 10)
    
    max_flow = flow_network.maximize_flow('s', 't')
    
    print(f"Maximum Flow achieved: {max_flow}\n")
    print("Final State of flow graph (Forward edges only):")
    
    for vertex in vertices:
        for edge in flow_network.adj_list[vertex]:
            if edge.capacity > 0:
                print(edge)
