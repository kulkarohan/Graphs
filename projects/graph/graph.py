"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

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

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        visited = set()

        q.enqueue(starting_vertex)
        
        # Visit nodes until queue is empty
        while q.size() > 0:
            current_node = q.dequeue()

            if current_node not in visited:
                # mark as visited
                visited.add(current_node)
                print(current_node)
                # get neighbors
                edges = self.get_neighbors(current_node)
                # put neighbors in line to be visited
                for edge in edges:
                    q.enqueue(edge)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        visited = set()

        # Put starting node on stack
        s.push(starting_vertex)
        
        # Visit nodes until queue is empty
        while s.size() > 0:
            # Get next node off top of stack
            current_node = s.pop()

            if current_node not in visited:
                # mark as visited
                visited.add(current_node)
                print(current_node)
                # get neighbors
                edges = self.get_neighbors(current_node)
                # put neighbors on stack to be visited
                for edge in edges:
                    s.push(edge)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        
        if starting_vertex not in visited:
            visited.add(starting_vertex)
            print(starting_vertex)

            for neighbor in self.get_neighbors(starting_vertex):
                self.dft_recursive(neighbor, visited)
        

        # visited.add(starting_vertex)

        # edges = self.get_neighbors(starting_vertex)

        # if len(edges) == 0:
        #     return
        
        # else:
        #     for edge in edges:
        #         if edge not in visited:
        #             self.dft_recursive(edge, visited)

 

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # make a queue
        q = Queue()
        # make a set for visited
        visited = set()

        # enqueue A PATH TO STARTING_VERTEX
        q.enqueue([starting_vertex])

        # while queue isn't empty
        while q.size() > 0:
            # dequeue the next path
            current_path = q.dequeue()
            # current_node is the last thing in the path
            current_node = current_path[-1]
            # check if its the target aka destination_vertex
            if current_node == destination_vertex:
                # if so, return path
                return current_path
            # if not, mark as visited
            else:
                if current_node not in visited:
                    visited.add(current_node)

                    edges = self.get_neighbors(current_node)

                    for edge in edges:
                        path_copy = list(current_path)
                        path_copy.append(edge)
                        q.enqueue(path_copy)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        visited = set()

        s.push([starting_vertex])

        while s.size() > 0:
            current_path = s.pop()
            current_node = current_path[-1]

            if current_node == destination_vertex:
                return current_path
            
            else:
                if current_node not in visited:
                    visited.add(current_node)

                    edges = self.get_neighbors(current_node)

                    for edge in edges:
                        path_copy = list(current_path)
                        path_copy.append(edge)
                        s.push(path_copy)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        
        if path is None:
            path = []

        if starting_vertex not in visited:
            visited.add(starting_vertex)
            path_copy = path.copy()
            path_copy.append(starting_vertex)

            if starting_vertex == destination_vertex:
                return path_copy
            
            for neighbor in self.get_neighbors(starting_vertex):
                new_path = self.dfs_recursive(neighbor, destination_vertex, visited, path_copy)

                if new_path is not None:
                    return new_path
        
        return None

        # if starting_vertex == destination_vertex:
        #     return [destination_vertex]
    
        # if starting_vertex not in visited:
        #     visited.add(starting_vertex)

        # for edge in edges:
        #     if edge

        # edges = self.get_neighbors(starting_vertex)

    # def dft_recursive(self, starting_vertex, visited=set()):
    #     """
    #     Print each vertex in depth-first order
    #     beginning from starting_vertex.

    #     This should be done using recursion.
    #     """
    #     visited.add(starting_vertex)

    #     edges = self.get_neighbors(starting_vertex)

    #     if len(edges) == 0:
    #         return
        
    #     else:
    #         for edge in edges:
    #             if edge not in visited:
    #                 self.dft_recursive(edge, visited)



if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
