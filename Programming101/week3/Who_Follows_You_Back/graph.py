
class Graph:

    def __init__(self):
        self.nodes = {}
        self.visited = []

    def add_edge(self, node_a, node_b):
        if node_a not in self.nodes.keys():
            self.nodes[node_a] = []
        if node_b not in self.nodes.keys():
            self.nodes[node_b] = []
        if node_b not in self.nodes[node_a]:
            self.nodes[node_a].append(node_b)

    def get_neighbours_for(self, node):
        if node in self.nodes.keys():
            return self.nodes[node]
        return []

    def path_between(self, node_a, node_b):
        if node_a not in self.nodes.keys() or node_b not in self.nodes.keys():
            return False
        if node_b in self.nodes[node_a]:
            return True

        self.visited.append(node_a)
        for item in self.nodes[node_a]:
            if item not in self.visited and self.path_between(item, node_b):
                print(self.visited)
                self.visited = []
                return True
            self.visited.append(item)
        return False

    def __str__(self):
        result = ""
        for key in sorted(self.nodes.keys()):
            result += "{}: {}".format(key, self.nodes[key]) + "\n"
        return result
