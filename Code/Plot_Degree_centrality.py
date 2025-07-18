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

# Degree Centrality
centrality = nx.degree_centrality(G)

# Sorting Result of the function
sorted_centrality = sorted(centrality.items(), key=lambda x: x[1], reverse=True)[:10]

#########################################################################################

# Print Top 10 Airports by Degree Centrality
print("Top 10 Airports by Degree Centrality:")
top_10_results = []
for i, (iata, centrality_value) in enumerate(sorted_centrality, start=1):
    airport_name = G.nodes[iata]['name']
    result = f"{i}. Airport: {iata} ({airport_name}), Centrality: {centrality_value:.4f}"
    top_10_results.append(result)
    print(result)

# Save the result in a txt file
with open('Degree_centrality.txt', 'w') as file:
    file.write("Top 10 Airports by Degree Centrality:\n")
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

# add less central nodes for data visualizzation
less_central_nodes = [node for node in G.nodes() if node not in dict(sorted_centrality)]
nx.draw_networkx_nodes(
    G, pos, nodelist=less_central_nodes, node_size=50, node_color='#adb5bd', alpha=0.5, ax=ax
)

# add top central nodes for data visualizzation first ten
top_central_nodes = [iata for iata, _ in sorted_centrality]
nx.draw_networkx_nodes(
    G, pos, nodelist=top_central_nodes,
    node_size=[centrality[node] * 6000 for node in top_central_nodes],
    node_color='#023e8a', alpha=0.95, ax=ax,
    edgecolors='white', linewidths=2
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
other_edges = [(u, v) for u, v in G.edges() if u not in top_central_nodes]

nx.draw_networkx_edges(G, pos, edgelist=other_edges, edge_color='#FF0000', alpha=0.1, arrows=False, ax=ax)
nx.draw_networkx_edges(G, pos, edgelist=top_edges, edge_color='#1E90FF', alpha=0.9, arrows=False, ax=ax)

# Title
plt.title('Flight Route Network - Top 10 Airports with Degree Centrality')
plt.xlabel('Longitude')
plt.ylabel('Latitude')

# Save Plot as a png
plt.savefig('Degree_Centrality.png', dpi=800)
plt.close()
#########################################################################################

# Calc Degree (numero totale di rotte in entrata + uscita)
degree = dict(G.degree())

# sort result
sorted_degree = sorted(degree.items(), key=lambda x: x[1], reverse=True)[:50]  # Top 50 aeroporti

#########################################################################################
# filtering nodes
top_10 = sorted_degree[:10]
others = sorted_degree[10:]

# create list for the plot
iata_top_10, values_top_10 = zip(*top_10)
iata_others, values_others = zip(*others)

# Posizioni per il grafico
x_top_10 = range(len(iata_top_10))
x_others = range(len(iata_top_10), len(iata_top_10) + len(iata_others))

#########################################################################################

# bar plot
plt.figure(figsize=(18, 10))

# Bar Top 10
plt.bar(
    x_top_10,
    values_top_10,
    color='#023e8a',
    edgecolor='black',
    label='Top 10 Aeroporti'
)

# Bar others
plt.bar(
    x_others,
    values_others,
    color='#adb5bd',
    edgecolor='#adb5bd',
    label='Altri Aeroporti (11-50)'
)

# AESTHETIC stuff label x y
plt.xlabel("Aeroporti (IATA)", fontsize=14)
plt.ylabel("Numero di Rotte (Degree)", fontsize=14)
plt.title("Top 50 Aeroporti per Numero di Rotte (Degree Centrality)", fontsize=16)

# label IATA
iata_labels = list(iata_top_10) + list(iata_others)
plt.xticks(
    ticks=range(len(iata_labels)),
    labels=iata_labels,
    fontsize=10,
    rotation=90
)

# Legend and grid
plt.legend(fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Save plot
plt.tight_layout()
plt.savefig('Degree_Centrality_Bar_Chart_Top_50', dpi=800)
plt.close()
#########################################################################################

