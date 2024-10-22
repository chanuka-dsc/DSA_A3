class ALGraph:

    def __init__(self, n_lst) -> None:
        # I used a dictionary here to make it easier to track the nodes compared to having indexes that will change when the list is updated
        self.adj = {n: [] for n in n_lst}

    # method to add an edge to the CONNECTED graph
    def add_edge(self, i: int, j):
        if j in self.adj.keys() and j not in self.adj.get(i):
            # Both cases are added to cover the connected graph behavior
            self.adj.get(i).append(j)
            self.adj.get(j).append(i)
            return True
        return False

    # method to remove and edge from the CONNECTED graph
    def remove_edge(self, i: int, j):
        if j in self.adj.keys() and j in self.adj.get(i):
            # Both cases are added to cover the connected graph behavior
            self.adj.get(i).remove(j)
            self.adj.get(j).remove(i)
            return True
        return False

    # method to add a node to the graph
    def add_node(self, n):
        self.adj[n] = []

    # method to remove a node to the graph
    def remove_node(self, n):

        for lst in self.adj.values():
            if n in lst:
                lst.remove(n)

        self.adj.pop(n)


""" Go to al_graph_tests to check the testing carried ou for this implementation"""
