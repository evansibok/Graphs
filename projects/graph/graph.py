"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

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
        else:
            raise IndexError("Vertex doesn't exist!")

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
        # Initialize queue
        q = Queue()
        # Add starting vertex to queue
        q.enqueue(starting_vertex)
        # Create a set to track visited vertices
        visited = set()
        # While queue is not empty
        while q.size() > 0:
            # dequeue item
            v = q.dequeue()
            # If removed item not in visited
            if v not in visited:
                # Add item to visited
                visited.add(v)
                print(v)
                # Get neighbors
                for next in self.vertices[v]:
                    # Add neighbors to queue
                    q.enqueue(next)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Initialize an empty stack
        s = Stack()
        # add the starting vertex to the stack
        s.push(starting_vertex)
        # Create a set to track visited vertices
        visited = set()
        # While stack isn't empty
        while s.size() > 0:
            # pop item
            v = s.pop()
            # if item hasn't been visited
            if v not in visited:
                # add item to visited
                visited.add(v)
                print(v)
                # get neighbors of item
                for next in self.get_neighbors(v):
                    # add them to queue
                    s.push(next)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        # Initial Case
        if visited is None:
            visited = set()

        # Base Case
        # How do we know we are done?
        # Ans: When we have no more neighbors
        # track visited nodes
        visited.add(starting_vertex)
        print(starting_vertex)

        # call recursively on the neighbors of the last vertex that hasn't been visited
        for next in self.get_neighbors(starting_vertex):
            if next not in visited:
                self.dft_recursive(next, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Initialize empty Queue
        q = Queue()
        # Add path to the queue
        q.enqueue([starting_vertex])
        # Create set to track visited
        visited = set()
        # While queue is empty
        while q.size() > 0:
            # dequeue path
            path = q.dequeue()
            print('path', path)
            # grab the last vertex from the removed path
            # and initialize to a variable
            last_v = path[-1]
            print("last_v", last_v)
            # if vertex is not in visited
            if last_v not in visited:
                # check if it is the target
                if last_v == destination_vertex:
                    # return the path to the target
                    return path
                # mark it visited
                visited.add(last_v)
                # add path to naighbours to back of queue
                for next in self.get_neighbors(last_v):
                    # copy the path (Copying the path returns in a bug)
                    # append the neighbor to the back of it
                    cp = path + [next]
                    print('cp', cp)
                    # add it to the queue
                    q.enqueue(cp)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Initialize an empty Stack
        s = Stack()
        # Add the starting vertex path to the stack
        s.push([starting_vertex])
        # Create a visited set to track vertices
        visited = set()
        # While Stack isn't empty
        while s.size() > 0:
            # pop the stack
            path = s.pop()
            # grab the last vertex from the popped vertex
            last_v = path[-1]
            # if it isn't in visited
            if last_v not in visited:
                # check if it is the target
                if last_v == destination_vertex:
                    # if it is
                    # return the path
                    return path
                # otherwise, add to visited
                visited.add(last_v)
                # get its neighbors
                for next in self.get_neighbors(last_v):
                    # copy the path and append the path to the neighbors
                    cp = path + [next]
                    # push the new path to the stack
                    s.push(cp)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # Initial Case
        if visited is None:
            visited = set()

        if path is None:
            path = []

        # After checking vertex, add it to visited
        visited.add(starting_vertex)
        # Add the path to neighbors to copy of existing path
        final_path = path + [starting_vertex]

        # Base case to step out of recursion
        if starting_vertex == destination_vertex:
            return final_path

        # call recursively on the neighbors of the last vertex that hasn't been visited
        for next in self.get_neighbors(starting_vertex):
            if next not in visited:
                path_to_neighbors = self.dfs_recursive(
                    next, destination_vertex, visited, final_path)
                if path_to_neighbors:
                    return path_to_neighbors


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
