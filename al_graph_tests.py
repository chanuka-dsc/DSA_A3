from ALGraph import ALGraph


def test_ALGraph():

    g = ALGraph([0, 1, 2, 3])
    assert g.adj == {0: [], 1: [], 2: [], 3: []}, "Failed Initialization Test"

    g.add_edge(0, 1)
    g.add_edge(2, 1)
    g.add_edge(3, 1)
    assert g.adj[0] == [1] and g.adj[1] == [0, 2, 3], "Failed Add Edge Test"

    g.add_node(4)
    assert 4 in g.adj and g.adj[4] == [], "Failed Add Node Test"

    g.add_edge(2, 3)
    g.remove_edge(2, 3)
    assert g.adj[2] == [1] and g.adj[3] == [1], "Failed Remove Edge Test"
    assert g.remove_edge(2, 3) == False, "Can not remove non existing elements"

    assert g.add_edge(0, 1) == False, "Adding duplicate edges is not expected in this"
    assert g.add_edge(2, 1) == False, "Adding duplicate edges is not expected in this"

    g.add_edge(0, 3)
    g.add_edge(3, 2)
    g.remove_node(1)
    assert (
        1 not in g.adj and 1 not in g.adj[0] and 1 not in g.adj[2]
    ), "Failed Remove Node Test"

    print("All tests passed.")


test_ALGraph()
