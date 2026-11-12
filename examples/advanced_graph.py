import ast
from pathlib import Path

import networkx as nx
import pandas as pd

DATA_DIR = Path("..", "..", "..", "data", "synergy_plus_extended")
DATASET = "Appenzeller-Herzog_2019"

df = pd.read_csv(DATA_DIR / f"{DATASET}.csv")

df["openalex_id"] = df["openalex_id"].str.lower()
df["referenced_works"] = df["referenced_works"].apply(
    lambda v: [w.lower() for w in ast.literal_eval(v)] if isinstance(v, str) and v else []
)

nodes = [(row.openalex_id, {"label_included": row.label_included}) for row in df.itertuples()]
edges = [(row.openalex_id, ref) for row in df.itertuples() for ref in row.referenced_works]

G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)
G.remove_nodes_from(set(G.nodes) - set(df["openalex_id"]))

print("Number of nodes", len(G.nodes))
print("Number of edges", len(G.edges))

nx.write_gexf(G, f"{DATASET}_network.gexf")
