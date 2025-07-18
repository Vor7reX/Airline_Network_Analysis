from Libraries import *

#########################################################################################
#Plot World Map of Airline Connections
# Create Graph
G = nx.DiGraph()

# Add Nodes and position
for index, row in Dataset.iterrows():
    G.add_node(row['IATA_x'], pos=(row['long_x'], row['lat_x']))
    G.add_node(row['IATA_y'], pos=(row['long_y'], row['lat_y']))

# Add Edges
for index, row in Dataset.iterrows():
    G.add_edge(row['IATA_x'], row['IATA_y'])

# Create Plot
plt.figure(figsize=(20, 16))
ax = plt.axes(projection=ccrs.PlateCarree())

# Graphics Elements for cartopy
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=':')
ax.add_feature(cfeature.LAND, color='#f8f1e4')
ax.gridlines(draw_labels=True, color='#f8f1e4', linestyle='--', alpha=0.5)


# Position nodes
pos = nx.get_node_attributes(G, 'pos')

# add nodes to the plot
nx.draw_networkx_nodes(G, pos, node_size=100, node_color='#023e8a', alpha=0.7, ax=ax)

# add edges to the plot
nx.draw_networkx_edges(G, pos, edge_color='#adb5bd', alpha=0.3, arrows=True, ax=ax)

# title and x y labels
plt.title('Flight Route Network')
plt.xlabel('Longitude')
plt.ylabel('Latitude')

# Save Plot
plt.savefig('world_plot.png', dpi=600)
plt.close()
#########################################################################################

