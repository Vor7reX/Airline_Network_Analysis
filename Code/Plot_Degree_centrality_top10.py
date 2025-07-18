from Libraries import *

#########################################################################################

# Create Graph
G = nx.DiGraph()

# Node with IATA code, geo Position and Airport Name
for index, row in Dataset.iterrows():
    G.add_node(row['IATA_x'], pos=(row['long_x'], row['lat_x']), name=row['airport.name_x'])
    G.add_node(row['IATA_y'], pos=(row['long_y'], row['lat_y']), name=row['airport.name_y'])

# Add Edges
for index, row in Dataset.iterrows():
    G.add_edge(row['IATA_x'], row['IATA_y'])

#########################################################################################

# Degree Centrality
centrality = nx.degree_centrality(G)

# Sorting Result of the function
sorted_centrality = sorted(centrality.items(), key=lambda x: x[1], reverse=True)[:10]

#########################################################################################

# Create subgraph
top_central_nodes = [iata for iata, _ in sorted_centrality]
top_10_G = G.subgraph(top_central_nodes).copy()

# Collect edges for top 10 nodes
top_edges = [(u, v) for u, v in G.edges() if u in top_central_nodes]

# Set of destination of the top ten
destination_nodes = set(v for _, v in top_edges if v not in top_central_nodes)

#########################################################################################

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

# Destination nodes
nx.draw_networkx_nodes(
    G, pos, nodelist=destination_nodes, node_size=50, node_color='#F77F00', alpha=0.5, ax=ax
)

# top ten nodes
nx.draw_networkx_nodes(
    top_10_G, pos, node_size=[centrality[node] * 6000 for node in top_10_G.nodes()],
    node_color='#023e8a', alpha=0.95, ax=ax,
    edgecolors='white', linewidths=2
)

# IATA CODE
for iata in top_central_nodes:
    x, y = pos[iata]
    plt.text(
        x, y, iata, fontsize=10, ha='center', va='center',
        color='white', bbox=dict(facecolor='#023e8a', edgecolor='none', boxstyle='circle,pad=0.2')
    )

# Edges
nx.draw_networkx_edges(top_10_G, pos, edgelist=top_edges, edge_color='#1E90FF', alpha=0.9, arrows=False, ax=ax)

# Title
plt.title('Flight Route Network - Only Top 10 Airports Degree Centrality')
plt.xlabel('Longitude')
plt.ylabel('Latitude')

# Save the plot as a png
plt.savefig('Degree_centrality_onlytopnodes.png', dpi=800)
plt.close()
#########################################################################################
