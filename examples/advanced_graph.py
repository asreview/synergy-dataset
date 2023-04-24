import networkx as nx

from synergy_dataset import Dataset

# load dataset
d = Dataset("Appenzeller-Herzog_2020")
result = d.to_dict(["id", "title", "referenced_works"])

# make collection of nodes and edges
nodes = [(k, {"label_included": v["label_included"]}) for k, v in result.items()]
edges = [(k, r) for k, v in result.items() for r in v["referenced_works"]]

# build the graph
G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)
G.remove_nodes_from(set(G.nodes) - set([n[0] for n in nodes]))

print("Number of nodes", len(G.nodes))
print("Number of edges", len(G.edges))

nx.write_gexf(G, "Appenzeller-Herzog_2020_network.gexf")
