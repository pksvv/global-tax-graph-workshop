# Calculate degree centrality for the undirected graph
degree_centrality = nx.degree_centrality(G)
print("Degree Centrality:")
for node, centrality in degree_centrality.items():
    print(f"{node}: {centrality:.2f}")


# Find the shortest path between USA and France in the undirected graph
shortest_path = nx.shortest_path(G, source="USA", target="France")
print("Shortest Path from USA to France:", " -> ".join(shortest_path))


# Calculate betweenness centrality for the directed graph
betweenness_centrality = nx.betweenness_centrality(DG)
print("Betweenness Centrality:")
for node, centrality in betweenness_centrality.items():
    print(f"{node}: {centrality:.2f}")
