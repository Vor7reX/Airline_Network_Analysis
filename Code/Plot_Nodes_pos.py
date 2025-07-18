from Libraries import *

#########################################################################################
# PLOT 0 Just Node with geo-position layout no map
# graph
G = nx.DiGraph()

# Add nodes to the graph with the geo position
for index, row in Dataset.iterrows():
    G.add_node(row['IATA_x'], pos=(row['long_x'], row['lat_x']))
    G.add_node(row['IATA_y'], pos=(row['long_y'], row['lat_y']))

# Add edges
for index, row in Dataset.iterrows():
    G.add_edge(row['IATA_x'], row['IATA_y'])

# Create Plot
plt.figure(figsize=(20, 16))

# nodes position
pos = nx.get_node_attributes(G, 'pos')

# add nodes
nx.draw_networkx_nodes(G, pos, node_size=100, node_color='#023e8a', alpha=0.7)

# add edges
nx.draw_networkx_edges(G, pos, edge_color='#adb5bd', alpha=0.3, arrows=True)

# Add Title
plt.title('Flight Route Network')


# Save Plot
plt.savefig('Nodes_pos.png', dpi=600)
plt.close()
#########################################################################################
