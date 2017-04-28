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
with open('data/project_data_final.csv', 'r') as edge_file:
    next(edge_file)
    for line in csv.reader(edge_file):
    	pair = (line[0], line[1])
    	edges.append(pair)
edge_file.close()

# SNA analysis
di_G = nx.DiGraph()
di_G.add_nodes_from(nodes)
di_G.nodes()

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

#individual analysis
print '##########################################################'
print ' The indegrees of Wong Ka Chun Anthony: ' , members_inDgree['16']
print ' The outdegree of Wong Ka Chun Anthony: ' , members_outDegree['16']
print ' The Betweeness of Wong Ka Chun Anthony: ' , betweeness['16']
print ' The Closeness of Wong Ka Chun Anthony: ' , closeness['16']

print '##########################################################'
print ' The indegrees of Law Yue Hei: ' , members_inDgree['15']
print ' The outdegree of Law Yue Hei: ' , members_outDegree['15']
print ' The Betweeness of Law Yue Hei: ' , betweeness['15']
print ' The Closeness of Law Yue Hei: ' , closeness['15']

print '##########################################################'

print ' The indegrees of Tse Ching Hin: ' , members_inDgree['40']
print ' The outdegree of Tse Ching Hin: ' , members_outDegree['40']
print ' The Betweeness of Tse Ching Hin: ' , betweeness['40']
print ' The Closeness of Tse Ching Hin: ' , closeness['40']


print '##########################################################'

print ' The indegrees of Wong Kam Shing: ' , members_inDgree['47']
print ' The outdegree of Wong Kam Shing: ' , members_outDegree['47']
print ' The Betweeness of Wong Kam Shing: ' , betweeness['47']
print ' The Closeness of Wong Kam Shing: ' , closeness['47']

