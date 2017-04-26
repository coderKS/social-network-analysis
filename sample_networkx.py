import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
# A directed Graph
di_G = nx.DiGraph()
# add one node
di_G.add_node(1)
# add multiple nodes
di_G.add_nodes_from ([2 ,3 ,4 ,5])
# the node ' s label can be string
di_G.add_node('Ted')
# check exsiting nodes in the graph
di_G.nodes()
#------ test
print "after adding nodes"
nx.draw(di_G)
plt.show()
#------


# remove nodes form the graph
di_G.remove_node('Ted')
# Check the nodes again
di_G.nodes ()

# add one edge (from node 1 to node 2)
di_G.add_edge(1 ,2)
# add multiple edges
edge_list = [(1, 4), (2, 3), (2, 4), (2, 5)]
di_G.add_edges_from(edge_list)
# remove an edge
di_G.remove_edge(2 ,5)
# check the edges
di_G.edges()

# Add an edge with weight
di_G.add_edge(3,4, weight=3)

# Add an edge with nonexist node
di_G.add_edge(3,6)
di_G.edges()
di_G.nodes()

# remove node 6
di_G.remove_node(6)
di_G.edges()

# Get Density for the graph
nx.density(di_G)
# Compute the Indegree
members_inDgree = di_G.in_degree()
# Compute the Outdegree
members_outDegree = di_G.out_degree()
print ' The indegrees for all nodes are: ' , members_inDgree
print ' The outdegree for all nodes are: ' , members_outDegree

# (Optional) Draw the graph using matplotlib
nx.draw(di_G)
plt.show()

