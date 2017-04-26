import csv
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

# init param
nodes = []
edges = []

# read node file
with open('data/node_data.csv', 'r') as node_file:
    next(node_file)
    for row in csv.reader(node_file):
    	nodes.append(row[0])
node_file.close()

# read edge file
with open('data/edge_raw_data.csv', 'r') as edge_file:
    next(edge_file)
    for line in csv.reader(edge_file):
    	pair = (line[0], line[1])
    	edges.append(pair)
edge_file.close()

# SNA analysis
di_G = nx.DiGraph()
di_G.add_nodes_from(nodes)
di_G.nodes()

# print "All nodes added"
# nx.draw(di_G)
# plt.show()

di_G.add_edges_from(edges)

# Get Density for the graph
density = nx.density(di_G)
# Compute the Indegree
members_inDgree = di_G.in_degree()
# Compute the Outdegree
members_outDegree = di_G.out_degree()
# Compute the Betweeness
betweeness = nx.betweenness_centrality(di_G)
# Compute the Closeness
closeness = nx.closeness_centrality(di_G)

print ' Density of the overall social network: ' , density
print ' The indegrees for all nodes are: ' , members_inDgree
print ' The outdegree for all nodes are: ' , members_outDegree
print ' The Betweeness for all nodes are: ' , betweeness
print ' The Closeness for all nodes are: ' , closeness

# print "All edges added"
# nx.draw(di_G)
# plt.show()
