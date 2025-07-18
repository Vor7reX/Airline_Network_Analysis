from Libraries import *

# i don't use this in my report but is interesting

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

# Eigenvector Centrality
eigenvector_centrality = nx.eigenvector_centrality(G, max_iter=1000)

# Sorting Result of the function
sorted_eigenvector = sorted(eigenvector_centrality.items(), key=lambda x: x[1], reverse=True)[:10]

#########################################################################################

# Print Top 10 Airports by Eigenvector Centrality
print("Top 10 Airports by Eigenvector Centrality:")
top_10_results = []
for i, (iata, centrality_value) in enumerate(sorted_eigenvector, start=1):
    airport_name = G.nodes[iata]['name']
    result = f"{i}. Airport: {iata} ({airport_name}), Centrality: {centrality_value:.4f}"
    top_10_results.append(result)
    print(result)

# Save the result in a txt file
with open('Eigenvector_Centrality.txt', 'w') as file:
    file.write("Top 10 Airports by Eigenvector Centrality:\n")
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

# Add less central nodes
less_central_nodes = [node for node in G.nodes() if node not in dict(sorted_eigenvector)]
nx.draw_networkx_nodes(
    G, pos, nodelist=less_central_nodes, node_size=50, node_color='#d1d5db', alpha=0.5, ax=ax
)

# Add top central nodes for data visualization (just the first ten)
top_central_nodes = [iata for iata, _ in sorted_eigenvector]
nx.draw_networkx_nodes(
    G, pos, nodelist=top_central_nodes,
    node_size=[eigenvector_centrality[node] * 6000 for node in top_central_nodes],
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

# Edges for the top central nodes and the other ones
top_edges = [(u, v) for u, v in G.edges() if u in top_central_nodes]
less_central_edges = [(u, v) for u, v in G.edges() if u in less_central_nodes and v in less_central_nodes]

nx.draw_networkx_edges(G, pos, edgelist=less_central_edges, edge_color='#004953', alpha=0.1, arrows=False, ax=ax)
nx.draw_networkx_edges(G, pos, edgelist=top_edges, edge_color='#6a0dad', alpha=0.9, arrows=False, ax=ax)

# Title
plt.title('Flight Route Network - Top 10 Airports by Eigenvector Centrality', fontsize=16)
plt.xlabel('Longitude')
plt.ylabel('Latitude')

# Save Plot as a png
plt.savefig('Eigenvector_Centrality.png', dpi=600)
plt.close()
#########################################################################################
#pie chart

# Calc percentages
total_centrality = sum(centrality_value for _, centrality_value in sorted_eigenvector)
percentages = [(iata, (centrality_value / total_centrality) * 100) for iata, centrality_value in sorted_eigenvector]

# data setting for the plot
labels = [f"{iata}" for iata, _ in percentages]
sizes = [centrality_value for _, centrality_value in percentages]
colors = sns.color_palette("viridis", len(sizes))

# plot
plt.figure(figsize=(10, 8))
wedges, _, autotexts = plt.pie(
    sizes,
    autopct='%.1f%%',
    startangle=140,
    colors=colors,
    wedgeprops={'edgecolor': 'black'}
)

# legend
plt.legend(wedges, labels, loc="upper right", fontsize=12, title="IATA", title_fontsize=14)

# usless stuff
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_weight('bold')
    autotext.set_fontsize(10)

# title
plt.title("Top 10 Aeroporti per Eigenvector Centrality", fontsize=16)

# save as png with dpi
plt.savefig('Eigenvector_Centrality_Pie_Chart.png', dpi=600)
plt.close()
#########################################################################################

