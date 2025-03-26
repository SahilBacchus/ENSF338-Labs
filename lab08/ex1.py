class GraphNode:
    def __init__(self, data):
        self.data = data
        self.edges = {}


class Graph:
    def __init__(self):
        self.nodes = {}

    def addNode(self, data):
        if data not in self.nodes:
            new_node = GraphNode(data)
            self.nodes[data] = new_node
            return new_node
        return None  
