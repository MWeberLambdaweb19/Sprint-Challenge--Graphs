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
        Add a directed edge to the graph from v1 to v2.
        """
        # Check if the vertices exist
        if v1 in self.vertices and v2 in self.vertices:
            # Add the edge
            self.vertices[v1].add(v2)
        else:
            print("ERROR: Could not add edge, vertex not found")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        # try:
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            return None
                # except ValueError
                # print(f"Vertex_id: {vertex_id} does not exist in the Graph vertices")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        BREADTH FIRST USES QUEUE
        """
        # Create a queue and enqueue starting vertex
        qq = Queue()
        qq.enqueue([starting_vertex])
        # test = "hello"
        # breakpoint()
        # pdb.set_trace()
        # Create a set of traversed vertices
        visited = set()
        # While queue is not empty:
        while qq.size() > 0:
            # dequeue/pop first vertex
            path = qq.dequeue()
            # if not visited
            if path[-1] not in visited:
                # PRINT IT
                print(path[-1])
                # mark as visited
                visited.add(path[-1]) 
                # enqueue neighbors
                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vert)
                    qq.enqueue(new_path)
                   
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        DEPTH FIRST USES STACK
        """
        st = Stack()
        st.push([starting_vertex])
        visited = set()
        while st.size() > 0:
            path = st.pop()
            if path[-1] not in visited:
                print(path[-1])
                visited.add(path[-1])
                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vert)
                    st.push(new_path)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        visited=set() YOU CAN'T DO THAT! 
        This visited cache will save whatever modifications made to it for each and every time it is used, for each function.

        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        ## CLASS WORK TO SEE ANOTHER WAY
        # Initial case
        if visited is None:
            visited = set()
            # this makes a set just for us to use in one function call

        # Base case
        # Track visited nodes

        visited.add(starting_vertex)
        print(starting_vertex)
        # Recurse the function - in a for loop!
        for neighbor in self.vertices[starting_vertex]:
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)
                # WATCH FOR SPELLING ERRORS


        # My work!
        # if visited is None:
            # visited = set()
        # if starting_vertex in visited:
        #     return
        # else: 
        #     visited.add(starting_vertex)
        #     print(starting_vertex)
        #     flanders = self.get_neighbors(starting_vertex)
        #     for neighborino in flanders:
        #         self.dft_recursive(neighborino, visited)
        # # print(starting_vertex)
        # st = Stack()
        # st.push(starting_vertex)
        # if starting_vertex not in st.stack:
        #     hiddidly_ho = self.get_neighbors(starting_vertex)
        #     for neighborino in hiddidly_ho:
        #         self.dft_recursive(neighborino) 
        # else:
        #     breakpoint()
        #     return 
        # st = Stack()
        # st.push([starting_vertex])
        # visited = set()
        # path = st.pop()
        # visited.add(path[-1])
        # recurring = self.get_neighbors(path[-1])
        # # breakpoint()
        # for neighborino in recurring:
        #     print(neighborino)
        #     print(visited)
        #     if neighborino not in visited:
        #         self.dft_recursive(neighborino)
        #     else:
        #         return 
    
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        
        Breadth-first uses Queues. BQ!
        """
        ## Understand
        # I want the shortest path from starting vertex to destination
        # breadth-first, which means a stack
        ### Notes from Breadth First Search video
        # Must explore all possible paths to find the shortest
        # Traverse across before down 
        # Does not revisit nodes

        qt = Queue()
        qt.enqueue([starting_vertex])
        visited = set()
        while qt.size() > 0:
            path = qt.dequeue()
            if path[-1] not in visited:
                # CLASS ANSWER
                if path[-1] == destination_vertex:
                    return path
                visited.add(path[-1])
                for neighborino in self.get_neighbors(path[-1]):
                    # MY WORK
                    # if neighborino == destination_vertex:
                    #     new_path = list(path)
                    #     new_path.append(neighborino)
                    #     return new_path
                    # else:
                    new_path = list(path)
                    new_path.append(neighborino)
                    qt.enqueue(new_path)

        # qt = Queue()
        # qt.enqueue([starting_vertex])
        # visited = set()
        # while qt.size() > 0:
        #     path = qt.dequeue()
        #     if path[-1] not in visited:
        #         visited.add(path[-1])

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        ### Notes from Depth First Search video
        # Must explore all possible paths to find the shortest
        # Traverse down before across
        # Does not revisit nodes
        st = Stack()
        st.push([starting_vertex])
        visited = set()
        while st.size() > 0:
            path = st.pop()
            if path[-1] not in visited:
                if path[-1] == destination_vertex:
                    return path
                visited.add(path[-1])
                for neighborino in self.get_neighbors(path[-1]):
                    # if neighborino == destination_vertex:
                    #     new_path = list(path)
                    #     new_path.append(neighborino)
                    #     return new_path
                    # else:
                    new_path = list(path)
                    new_path.append(neighborino)
                    st.push(new_path)

    # def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
    #     # CLASS VERSION
    #     if visited is None:
    #         visited = set()

    #     if path is None:
    #         path = [] # or list()

    #     visited.add(starting_vertex)
    #     new_path = path + [starting_vertex]

    #     if starting_vertex == destination_vertex:
    #         return new_path

    #     for neighbor in self.vertices[starting_vertex]:
    #         if neighbor not in visited:
    #             neighbor_path = self.dfs_recursive(neighbor, destination_vertex, visited, new_path)
    #             if neighbor_path:
    #                 return neighbor_path
    def dfs_recursive(self, starting_vertex, destination_vertex, path=None, visited=None):
        # MINE! DOESN'T WORK!
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        ### Notes from Depth First Search video
        # Must explore all possible paths to find the shortest
        # Traverse down before across
        # Does not revisit nodes
        if path is None:
            path = list()
        if visited is None:
            visited = set()
        if starting_vertex not in visited:
            visited.add(starting_vertex)
            # THIS WAS AN ISSUE: I WAS NOT COPYING MY PATH
            path = path + [starting_vertex]
            if starting_vertex == destination_vertex:
                return path
        
            for neighborino in self.get_neighbors(starting_vertex):
                cat = self.dfs_recursive(neighborino, destination_vertex, path, visited)
                if cat:
                    # HAD TO RETURN THIS IF IT EXISTS
                    return cat

    #     if starting_vertex in visited:
    #         return None

        # if destination_vertex in self.get_neighbors(starting_vertex):
        #     new_path = path + [starting_vertex]
        #     return new_path
        # else:
        #     new_path = path + [starting_vertex]
        #     visited.add(starting_vertex)
        #     for neighborino in self.get_neighbors(starting_vertex):
        #         return self.dfs_recursive(neighborino, destination_vertex, path, visited)
        # if starting_vertex in visited:
        #     return 
        # else:
        #     if starting_vertex == destination_vertex:
        #         path.append(starting_vertex)
        #         cat = 7
        #         return cat
        #     else:
        #         visited.add(starting_vertex)
        #         path.append(starting_vertex)
        #     for neighborino in self.get_neighbors(starting_vertex): 
        #         self.dfs_recursive(neighborino, destination_vertex, path, visited)

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

    # '''
    # Should print:
    #     {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    # '''
    # print(graph.vertices)

    # '''
    # Valid BFT paths:
    #     1, 2, 3, 4, 5, 6, 7
    #     1, 2, 3, 4, 5, 7, 6
    #     1, 2, 3, 4, 6, 7, 5
    #     1, 2, 3, 4, 6, 5, 7
    #     1, 2, 3, 4, 7, 6, 5
    #     1, 2, 3, 4, 7, 5, 6
    #     1, 2, 4, 3, 5, 6, 7
    #     1, 2, 4, 3, 5, 7, 6
    #     1, 2, 4, 3, 6, 7, 5
    #     1, 2, 4, 3, 6, 5, 7
    #     1, 2, 4, 3, 7, 6, 5
    #     1, 2, 4, 3, 7, 5, 6
    # '''
    # graph.bft(1)

    # '''
    # Valid DFT paths:
    #     1, 2, 3, 5, 4, 6, 7
    #     1, 2, 3, 5, 4, 7, 6
    #     1, 2, 4, 7, 6, 3, 5
    #     1, 2, 4, 6, 3, 5, 7
    # '''
    # graph.dft(1)
    # graph.dft_recursive(1)

    # '''
    # Valid BFS path:
    #     [1, 2, 4, 6]
    # '''
    # print(graph.bfs(1, 6))

    # '''
    # Valid DFS paths:
    #     [1, 2, 4, 6]
    #     [1, 2, 4, 7, 6]
    # '''
    # print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))

