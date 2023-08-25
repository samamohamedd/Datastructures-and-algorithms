class graph:  # undirected
    def __init__(self) -> None:
        self.numOfNodes = 0
        self.adjacentList = {}

    def addVertex(self, node):
        if node not in self.adjacentList.keys():
            self.adjacentList[node] = set()
        else:
            print("already exist")

    def addEdge(self, node1, node2):
        if node1 in self.adjacentList and node2 in self.adjacentList:
            self.adjacentList[node1].add(node2)
            self.adjacentList[node2].add(node1)
        else:
            print("one or both the nodes does not exist")

    def showConnections(self):
        for item in self.adjacentList.keys():
            print(f"{item} : {self.adjacentList[item]}")


mygraph = graph()
mygraph.addVertex("0")
mygraph.addVertex("1")
mygraph.addVertex("2")
mygraph.addVertex("3")
mygraph.addVertex("4")
mygraph.addVertex("5")
mygraph.addVertex("6")
mygraph.addEdge("0", "2")
mygraph.addEdge("0", "1")
mygraph.addEdge("1", "2")
mygraph.addEdge("1", "3")
mygraph.addEdge("2", "4")
mygraph.addEdge("3", "4")
mygraph.addEdge("4", "5")
mygraph.addEdge("5", "6")

mygraph.showConnections()
