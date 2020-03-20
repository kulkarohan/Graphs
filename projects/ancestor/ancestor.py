from util import Queue


class Graph:
    """
    Represent a graph as a dictionary of vertices mapping labels to edges.
    """
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

def earliest_ancestor(ancestors, starting_node):
    g = Graph()
    q = Queue()
    visited = []

    # Add nodes (vertices) into graph
    for parent_child in ancestors:
        for node in parent_child:
            g.add_vertex(node)

    # Connect parent-child with edges
    for parent_child in ancestors:
        # Add key:value in dictionary as child:parent
        g.add_edge(parent_child[1], parent_child[0])

    # Begin BFT
    q.enqueue(starting_node)

    while q.size() > 0:
        current_node = q.dequeue()

        if current_node not in visited:
            visited.append(current_node)
            edges = g.get_neighbors(current_node)

            if edges:
                for edge in edges:
                    q.enqueue(edge)
            # if current_node has no neighbors it has no ancestor
            else:
                # append -1 to array to signify no ancestor
                visited.append(-1)

    # If starting_node has no ancestor, return -1
    if len(visited) == 2:
        return visited[-1]
    # Else return the earliest ancestor
    else:
        return visited[-2]



if __name__ == "__main__":
    test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                      (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    print(earliest_ancestor(test_ancestors, 6))
