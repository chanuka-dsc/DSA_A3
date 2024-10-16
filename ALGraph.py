class ALGraph:

    def __init__(self, n_lst) -> None:
        self.adj = {n: [] for n in n_lst}

    def add_edge(self, i: int, j):
        if j in self.adj.keys() and j not in self.adj.get(i):
            self.adj.get(i).append(j)
            self.adj.get(j).append(i)
            return True
        return False

    def remove_edge(self, i: int, j):
        if j in self.adj.keys() and j in self.adj.get(i):
            self.adj.get(i).remove(j)
            self.adj.get(j).remove(i)
            return True
        return False

    def add_node(self, n):
        self.adj[n] = []

    def remove_node(self, n):

        for lst in self.adj.values():
            if n in lst:
                lst.remove(n)

        self.adj.pop(n)
