the import issue at linked list and llnode

indexing starts at one

tried the quick sort in lecture, had issues used abdul biharis one

# def DFS(graph: ALGraph, search_node):

# visited = set()

# for v in graph.adj:

# result = DFS_helper(graph, v, search_node, visited)

# if result is not None:

# return result

# return None

# def DFS_helper(graph: ALGraph, node, search_node, visited):

# visited.add(node)

# print(node, " ---> ", end="")

# if node == search_node:

# print("found !!!")

# return node

# for neighbor in graph.adj.get(node, []):

# if neighbor not in visited:

# result = DFS_helper(graph, neighbor, search_node, visited)

# if result is not None:

# return result

# return None
