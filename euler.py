class Euler:
    vertices = 0
    graph_list = []
    successors = []
    ins = []
    outs = []

    def __init__(self, vertices, graph_list):
        self.vertices = vertices
        self.graph_list = graph_list
        self.ins = [0] * (vertices + 1)
        self.outs = [0] * (vertices + 1)
        self.successors = self.load_successors()
        print("\nHello from Euler")
        if self.euler_exists():
            print("Euler cycle exists")
            print(*self.find_euler())
        else:
            print("There's no euler cycle. Sorry :(")

    def load_successors(self):
        successors = [[] for _ in range(self.vertices)]
        for edge in self.graph_list:
            successors[edge[0] - 1].append(edge[1])

        return list(map(sorted, successors))

    def euler_exists(self):
        for connection in self.graph_list:
            self.ins[connection[1]] += 1
            self.outs[connection[0]] += 1
        for i in range(self.vertices + 1):
            if self.ins[i] - self.outs[i] != 0:
                return False
            if self.outs[i] - self.ins[i] != 0:
                return False
        return True

    def find_euler(self):
        visiting_path = [1]
        euler_cycle = []

        while visiting_path:
            vertex = visiting_path[-1]

            if self.successors[vertex - 1]:
                next_vertex = self.successors[vertex - 1].pop()
                visiting_path.append(next_vertex)
            else:
                euler_cycle.append(visiting_path.pop())

        return reversed(euler_cycle)
