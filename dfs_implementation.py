from ALGraph import ALGraph

n_lst = [1, 2, 3, 4, 5, 6, 7]
g = ALGraph(n_lst)
g.add_edge(2, 5)
g.add_edge(1, 2)
g.add_edge(1, 4)
g.add_edge(4, 3)
g.add_edge(5, 1)
g.add_edge(6, 3)


# print the current graph
print(g.adj)


def DFS(graph: ALGraph, start_node, search_node, visited):
    visited.add(start_node)
    print(start_node, " ---> ", end="")

    if start_node == search_node:
        print("found !!!")
        return search_node

    for v in graph.adj.get(start_node):
        if v not in visited:
            result = DFS(graph, v, search_node, visited)

            if result is not None:
                return result  # otherwise it will run after finding if there are any more adjacent nodes in the list left


# Testing to search the same node with different starting points
print("\n!----Search for 6 from 1----!")
print("Expected: 1  ---> 2  ---> 5  ---> 4  ---> 3  ---> 6  ---> found !!!")
print("Actual: ", end="")
DFS(g, 1, 6, set())

print("\n!----Search for 6 from 2----!")
print("Expected: 2  ---> 5  ---> 1  ---> 4  ---> 3  ---> 6  ---> found !!!")
print("Actual: ", end="")
DFS(g, 2, 6, set())

print("\n!----Search for 6 from 3----!")
print("Expected:  3  ---> 4  ---> 1  ---> 2  ---> 5  ---> 6  ---> found !!!")
print("Actual: ", end="")
DFS(g, 3, 6, set())

# Case where first neighbor node is the expected node
print("\n!----Search for 5 from 2----!")
print("Expected:  2  ---> 5  ---> found !!!")
print("Actual: ", end="")
DFS(g, 2, 5, set())

# Case where there is no link to the searched node
print("\n!----Search for 7 from 2----!")
print("Expected: 2  ---> 5  ---> 1  ---> 4  ---> 3  ---> 6  --->  None")
print("Actual: ", end="")
print(DFS(g, 2, 7, set()))
