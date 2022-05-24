class Hamilton:
    vertices = 0
    graph_list = []
    successors = []
    ins = []
    outs = []
    found_path = [1]
    visited = []
    visited_count = 0
    path_current = 1

    def __init__(self, vertices, graph_list):
        self.vertices = vertices
        self.graph_list = graph_list
        self.ins = [0] * vertices
        self.outs = [0] * vertices
        print("\nHello from Hamilton")
        if self.hamilton_exists():
            self.successors = self.load_successors()
            self.check_cycle()
        else:
            print("No hamilton. Necessary condition not met!")

    def hamilton_exists(self):
        for connection in self.graph_list:
            self.ins[connection[1] - 1] += 1
            self.outs[connection[0] - 1] += 1
        for i in range(self.vertices + 1):
            if self.ins[i - 1] == 0:
                return False
            if self.outs[i - 1] == 0:
                return False
        return True

    def load_successors(self):
        successors = [[] for _ in range(self.vertices)]
        for edge in self.graph_list:
            successors[edge[0] - 1].append(edge[1])

        return list(map(sorted, successors))

    def check_cycle(self):
        self.visited = [False] * self.vertices

        if self.hamilton_cycle(1):
            print("Found cycle :)")
            print(*self.found_path)
        else:
            print("Couldn't find the hamiltonian cycle :(")

    def hamilton_cycle(self, current_position):
        self.visited[current_position - 1] = True
        self.visited_count += 1
        for vertex in self.successors[current_position - 1]:
            if vertex == 1 and self.visited_count == self.vertices:
                self.found_path.append(vertex)
                return True
            if not self.visited[vertex - 1]:
                self.found_path.append(vertex)
                if self.hamilton_cycle(vertex):
                    return True
        self.found_path.pop()
        self.visited[current_position - 1] = False
        self.visited_count -= 1
        return False
