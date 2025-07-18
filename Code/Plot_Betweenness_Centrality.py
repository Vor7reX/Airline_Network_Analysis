from Libraries import *


#########################################################################################

# Graph
G = nx.DiGraph()

# Node with IATA code, geo Position and Airport Name
for index, row in Dataset.iterrows():
    G.add_node(row['IATA_x'], pos=(row['long_x'], row['lat_x']), name=row['airport.name_x'])
    G.add_node(row['IATA_y'], pos=(row['long_y'], row['lat_y']), name=row['airport.name_y'])

# Add Edges
for index, row in Dataset.iterrows():
    G.add_edge(row['IATA_x'], row['IATA_y'])

#########################################################################################

# function Betweenness Centrality
betweenness_centrality = nx.betweenness_centrality(G)

# Sorting Result of the function
sorted_betweenness = sorted(betweenness_centrality.items(), key=lambda x: x[1], reverse=True)[:10]

#########################################################################################

# Print Top 10 Airports by Betweenness Centrality maybe serve later
print("Top 10 Airports by Betweenness Centrality:")
top_10_results = []
for i, (iata, centrality_value) in enumerate(sorted_betweenness, start=1):
    airport_name = G.nodes[iata]['name']
    result = f"{i}. Airport: {iata} ({airport_name}), Centrality: {centrality_value:.4f}"
    top_10_results.append(result)
    print(result)

# Save the result in a txt file
with open('Betweenness_Centrality.txt', 'w') as file:
    file.write("Top 10 Airports by Betweenness Centrality:\n")
    file.write("\n".join(top_10_results))

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

# add less central nodes for data visualization
less_central_nodes = [node for node in G.nodes() if node not in dict(sorted_betweenness)]
nx.draw_networkx_nodes(
    G, pos, nodelist=less_central_nodes, node_size=50, node_color='#d1d5db', alpha=0.5, ax=ax
)

# add top central nodes for data visualizzation first ten
top_central_nodes = [iata for iata, _ in sorted_betweenness]
nx.draw_networkx_nodes(
    G, pos, nodelist=top_central_nodes,
    node_size=[betweenness_centrality[node] * 6000 for node in top_central_nodes],
    node_color='#023e8a', alpha=0.95, ax=ax,
    edgecolors='white', linewidths=2.5
)


# Add IATA code for the top central nodes
for iata in top_central_nodes:
    x, y = pos[iata]
    plt.text(
        x, y, iata, fontsize=10, ha='center', va='center',
        color='white', bbox=dict(facecolor='#023e8a', edgecolor='none', boxstyle='circle,pad=0.2')
    )

# Edges for the top central nodes and the other one
top_edges = [(u, v) for u, v in G.edges() if u in top_central_nodes]
less_central_edges = [(u, v) for u, v in G.edges() if u in less_central_nodes and v in less_central_nodes]

# Aesthetic stuff
nx.draw_networkx_edges(G, pos, edgelist=less_central_edges, edge_color='#004953', alpha=0.1, arrows=False, ax=ax)
nx.draw_networkx_edges(G, pos, edgelist=top_edges, edge_color='#10b981', alpha=0.9, arrows=False, ax=ax)


# Title and labels x y
plt.title('Flight Route Network - Top 10 Airports by Betweenness Centrality')
plt.xlabel('Longitude')
plt.ylabel('Latitude')

# Save Plot as a png
plt.savefig('Betweenness_Centrality.png', dpi=800)
plt.close()

#########################################################################################



