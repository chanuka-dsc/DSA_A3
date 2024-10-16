from ALGraph import ALGraph

n_lst = [1, 2, 3, 4, 5, 6]
g = ALGraph(n_lst)
g.add_edge(2, 5)
g.add_edge(2, 7)
g.add_edge(3, 7)  # this should not add
g.add_edge(1, 2)
g.add_edge(1, 4)
g.add_edge(5, 1)
g.add_edge(6, 3)

print(g.adj)


# def DFS_selected(graph: ALGraph, start_node, search_node, visited=set()):
#     visited.add(start_node)
#     print(start_node, " ---> ", end="")

#     if start_node == search_node:
#         print("found !!!")
#         return search_node

#     for v in graph.adj.get(start_node):
#         if v not in visited:
#             DFS(graph, v, search_node, visited)


# # DFS_selected(g, 1, 3)


def DFS(graph: ALGraph, search_node):
    visited = set()
    for v in graph.adj:

        result = DFS_helper(graph, v, search_node, visited)

        if result is not None:
            return result

    return None


def DFS_helper(graph: ALGraph, node, search_node, visited):
    visited.add(node)
    print(node, " ---> ", end="")

    if node == search_node:
        print("found !!!")
        return node

    for neighbor in graph.adj.get(node, []):
        if neighbor not in visited:
            result = DFS_helper(graph, neighbor, search_node, visited)

            if result is not None:
                return result

    return None


# sill be with first node itself
print("\n!----Search for 1----!")
print("Expected:  1  ---> found !!!")
print("Actual: ", end="")
DFS(g, 1)

# second one because first neighbor of 1
print("\n!----Search for 2----!")
print("Expected: 1  ---> 2  --->  found !!!")
print("Actual: ", end="")
DFS(g, 2)

# Have to wait till all the neighbors of nodes 1 and 2 and their neighbors and so on are searched as only element with an edge to 3 is 6 whish is not 3 itself
print("\n!----Search for 3----!")
print("Expected:  1  ---> 2  ---> 5  ---> 4  ---> 2  ---> 3  found !!!")
print("Actual: ", end="")
DFS(g, 3)

# Have to wait till all neighbors of 2 is done and comes back to 1's neighbors and where after two is 4
print("\n!----Search for 4----!")
print("Expected:  1  ---> 2  ---> 5  ---> 4   ---> found !!!")
print("Actual: ", end="")
DFS(g, 4)

# first neighbor to 2
print("\n!----Search for 5----!")
print("Expected:  1  ---> 2  ---> 5  ---> found !!!")
print("Actual: ", end="")
DFS(g, 5)

# first neighbor to 3
print("\n!----Search for 6----!")
print("Expected:  1  ---> 2  ---> 5  ---> 4  ---> 2  ---> 3  ---> 6  ---> found !!!")
print("Actual: ", end="")
DFS(g, 6)
