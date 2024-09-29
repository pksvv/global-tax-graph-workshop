# Load the financial flows dataset
financial_flows = pd.read_csv('financial_flows.csv')

# Create a directed graph
DG = nx.DiGraph()

# Add edges from the dataset
for _, row in financial_flows.iterrows():
    DG.add_edge(row['From_Company'], row['To_Company'], amount=row['Amount_USD'], transaction_type=row['Transaction_Type'])

# Define node positions for better visualization
pos = nx.spring_layout(DG, seed=42)  # Seed for reproducibility

# Draw the directed graph
plt.figure(figsize=(8,6))
nx.draw_networkx_nodes(DG, pos, node_color='lightgreen', node_size=1500)
nx.draw_networkx_edges(DG, pos, edge_color='black', arrows=True, arrowstyle='->', arrowsize=20)
nx.draw_networkx_labels(DG, pos, font_size=12, font_weight='bold')

# Add edge labels for transaction types and amounts
edge_labels = {(u, v): f"{d['transaction_type']} (${d['amount']})" for u, v, d in DG.edges(data=True)}
nx.draw_networkx_edge_labels(DG, pos, edge_labels=edge_labels, font_color='blue')

plt.title("Financial Flows Between Companies")
plt.axis('off')
plt.show()
