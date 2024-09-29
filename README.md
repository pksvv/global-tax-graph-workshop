# global-tax-graph-workshop
Global Tax Graph Workshop: A hands-on guide to applying graph theory in global taxation. This repository provides Python scripts, datasets, and resources to create, visualize, and analyze tax and financial networks using networkx. Topics include graph metrics, transfer pricing, tax compliance, and financial flows.
# Global Tax Graph Workshop

**A hands-on guide to applying graph theory in global taxation.**

This repository contains Python scripts, datasets, and resources to help you explore how graph theory can be applied to global taxation and financial networks. Through real-world examples and datasets, you'll learn how to create, visualize, and analyze tax-related networks using tools like `networkx` and Python.

## Structure
global-tax-graph-workshop/
├── datasets/
│   ├── tax_treaties.csv
│   ├── financial_flows.csv
│   └── sales_transactions.csv
├── notebooks/
│   ├── Module1_Graph_Theory.ipynb
│   ├── Module2_NLP_Extraction.ipynb
│   └── Module3_Knowledge_Graphs_Neo4j.ipynb
├── scripts/
│   ├── visualize_degree_centrality.py
│   ├── export_metrics.py
│   └── ...
├── README.md
└── LICENSE

## About

This workshop focuses on:
- **Creating graphs** (undirected and directed) to represent tax and financial systems.
- **Visualizing networks** to understand connections between entities (countries, companies, transactions).
- **Computing graph metrics** such as degree centrality, betweenness centrality, and shortest path to analyze the roles of different nodes in a network.
- **Understanding global tax systems**, transfer pricing, tax compliance, and financial flows through the lens of graph theory.

## Datasets

The following datasets are included:
1. **City Routes** (`city_routes.csv`): Represents undirected routes between cities.
2. **Financial Flows** (`financial_flows.csv`): Represents directed financial flows between countries.

You can use these datasets to build and visualize networks, compute metrics, and experiment with graph analysis techniques.

## Installation

Before running the code, ensure you have the required Python libraries installed. Use the following command to install the necessary dependencies:

```bash
!pip install networkx matplotlib pandas
