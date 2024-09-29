# Import necessary libraries
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

# Load the tax treaties dataset
tax_treaties = pd.read_csv('tax_treaties.csv')

# Create an undirected graph
G = nx.Graph()

# Add edges from the dataset
for _, row in tax_treaties.iterrows():
    G.add_edge(row['Country_A'], row['Country_B'], treaty_type=row['Treaty_Type'], effective_rate=row['Effective_Rate'])

# Define node positions for better visualization
pos = nx.spring_layout(G, seed=42)  # Seed for reproducibility

# Draw the graph
plt.figure(figsize=(8,6))
nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=1500)
nx.draw_networkx_edges(G, pos, edge_color='gray', width=2)
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')

# Add edge labels for treaty types
edge_labels = {(u, v): d['treaty_type'] for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

plt.title("Bilateral Tax Treaties Between Countries")
plt.axis('off')
plt.show()