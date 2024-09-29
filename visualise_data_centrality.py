# Calculate degree centrality
degree_centrality = nx.degree_centrality(G)

# Define node sizes based on degree centrality
node_sizes = [1000 * degree_centrality[node] for node in G.nodes()]

# Draw the graph with node sizes reflecting degree centrality
plt.figure(figsize=(8,6))
nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=node_sizes)
nx.draw_networkx_edges(G, pos, edge_color='gray', width=2)
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')

# Add edge labels
edge_labels = {(u, v): d['treaty_type'] for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

plt.title("Bilateral Tax Treaties with Degree Centrality")
plt.axis('off')
plt.show()

# Export degree centrality to CSV
degree_df = pd.DataFrame(list(degree_centrality.items()), columns=['Country', 'Degree_Centrality'])
degree_df.to_csv('degree_centrality.csv', index=False)
print("Degree centrality exported to degree_centrality.csv")

# Export betweenness centrality to CSV
betweenness_df = pd.DataFrame(list(betweenness_centrality.items()), columns=['Company', 'Betweenness_Centrality'])
betweenness_df.to_csv('betweenness_centrality.csv', index=False)
print("Betweenness centrality exported to betweenness_centrality.csv")
