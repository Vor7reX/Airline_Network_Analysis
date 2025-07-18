import matplotlib.pyplot as plt

from Libraries import *

# Graph
G = nx.DiGraph()

# Node with IATA code, geo Position, and Airport Name
for index, row in Dataset.iterrows():
    G.add_node(row['IATA_x'], pos=(row['long_x'], row['lat_x']), name=row['airport.name_x'])
    G.add_node(row['IATA_y'], pos=(row['long_y'], row['lat_y']), name=row['airport.name_y'])

# Add Edges
for index, row in Dataset.iterrows():
    G.add_edge(row['IATA_x'], row['IATA_y'])

#########################################################################################

# Betweenness Centrality
betweenness_centrality = nx.betweenness_centrality(G)

# Sorting Result of the function
sorted_betweenness = sorted(betweenness_centrality.items(), key=lambda x: x[1], reverse=True)[:10]

# Degree Centrality
degree_centrality = nx.degree_centrality(G)

# Sorting Result of the function
sorted_degree = sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)[:10]

#########################################################################################

# intersection of the top 10 airports by both centralities
top_betweenness_airports = {iata for iata, _ in sorted_betweenness}
top_degree_airports = {iata for iata, _ in sorted_degree}
common_airports = top_betweenness_airports & top_degree_airports

#########################################################################################

# Create Plot
plt.figure(figsize=(20, 16))
ax = plt.axes(projection=ccrs.PlateCarree())

# Graphics Elements for cartopy
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=':')
ax.add_feature(cfeature.LAND, color='#f8f1e4')
ax.gridlines(draw_labels=True, color='#f8f1e4', linestyle='--', alpha=0.5)

# add Position nodes
pos = nx.get_node_attributes(G, 'pos')

# other airport
nx.draw_networkx_nodes(
    G, pos, nodelist=[node for node in G.nodes() if node not in common_airports],
    node_size=50, node_color='#d1d5db', alpha=0.5, ax=ax
)

# Add central nodes for data visualization
nx.draw_networkx_nodes(
    G, pos, nodelist=list(common_airports),
    node_size=[betweenness_centrality[node] * 6000 for node in common_airports],
    node_color='#023e8a', alpha=0.95, ax=ax,
    edgecolors='white', linewidths=2.5
)

# Add IATA code
for iata in common_airports:
    x, y = pos[iata]
    plt.text(
        x, y, iata, fontsize=10, ha='center', va='center',
        color='white', bbox=dict(facecolor='#023e8a', edgecolor='none', boxstyle='circle,pad=0.2')
    )

# Add edges
common_edges = [(u, v) for u, v in G.edges() if u in common_airports or v in common_airports]
nx.draw_networkx_edges(G, pos, edgelist=common_edges, edge_color='#40E0D0', alpha=0.9, arrows=True, ax=ax)

# Title and labelss
plt.title('Flight Route Network - Common Top Airports by Betweenness & Degree Centrality', fontsize=16)
plt.xlabel('Longitude')
plt.ylabel('Latitude')

# Save Plot as a PNG
plt.savefig('Common_Centrality_Routes.png', dpi=600)
plt.close()

#########################################################################################

# Calcolo della correlazione tra Degree Centrality e Betweenness Centrality

# create dataframe
centrality_df = pd.DataFrame({
    'IATA': list(degree_centrality.keys()),
    'Degree_Centrality': list(degree_centrality.values()),
    'Betweenness_Centrality': list(betweenness_centrality.values())
})

# Calc
correlation = centrality_df['Degree_Centrality'].corr(centrality_df['Betweenness_Centrality'])


# print correlazione
print(f"Correlazione tra Degree Centrality e Betweenness Centrality: {correlation:.4f}")

#########################################################################################

# Scatter Plot with linear regression
plt.figure(figsize=(8, 6))


intersection = top_betweenness_airports & top_degree_airports
only_degree = top_degree_airports - intersection
only_betweenness = top_betweenness_airports - intersection

# dataframe for the plot
centrality_df['Category'] = centrality_df['IATA'].apply(
    lambda iata: 'Common' if iata in intersection else
    'Only Degree' if iata in only_degree else
    'Only Betweenness' if iata in only_betweenness else 'Other'
)

# using seaborn for linear regression
sns.regplot(
    x='Degree_Centrality', y='Betweenness_Centrality', data=centrality_df,
    scatter=False, line_kws={'color': '#E7756D', 'label': 'Regressione'}
)

# add nodes with different colour for better data visualization
colors_map = {
    'Common': '#023e8a',
    'Only Degree': '#CCFF00',
    'Only Betweenness': '#00FFFF',
    'Other': '#696969'
}
for category, color in colors_map.items():
    subset = centrality_df[centrality_df['Category'] == category]
    plt.scatter(
        subset['Degree_Centrality'], subset['Betweenness_Centrality'],
        color=color, alpha=0.7, s=45, label=category
    )

#IATA
for _, row in centrality_df.iterrows():
    if row['Category'] != 'Other':  # Annotare solo i nodi principali
        plt.text(
            row['Degree_Centrality'], row['Betweenness_Centrality'], row['IATA'],
            fontsize=10, ha='right', color='black'
        )

# labels and title
plt.xlabel('Degree Centrality', fontsize=10)
plt.ylabel('Betweenness Centrality', fontsize=10)
plt.title('Correlation Degree vs Betweenness Centrality with linear regression', fontsize=12)
plt.grid(alpha=0.3)

# Legenda
plt.legend(
    loc='upper left', bbox_to_anchor=(1, 1), fontsize=10
)

# Save  plot as png
plt.savefig('Scatter_Plot_with_Regression_and_Area.png', dpi=600, bbox_inches='tight')
plt.close()


#########################################################################################
# create file
with open('Airport_Details.txt', 'w') as file:
    file.write("Dettagli degli aeroporti:\n\n")

    # print common airport
    file.write("Aeroporti comuni (sia in Betweenness che Degree Centrality):\n")
    print("\nAeroporti comuni:")
    for iata in common_airports:
        airport_name = G.nodes[iata]['name']
        print(f"  - {iata}: {airport_name}")
        file.write(f"  - {iata}: {airport_name}\n")

    # print only degree airport
    file.write("\nAeroporti solo in Degree Centrality:\n")
    print("\nAeroporti solo in Degree Centrality:")
    for iata in only_degree:
        airport_name = G.nodes[iata]['name']
        print(f"  - {iata}: {airport_name}")
        file.write(f"  - {iata}: {airport_name}\n")

    # print only betweenness airport
    file.write("\nAeroporti solo in Betweenness Centrality:\n")
    print("\nAeroporti solo in Betweenness Centrality:")
    for iata in only_betweenness:
        airport_name = G.nodes[iata]['name']
        print(f"  - {iata}: {airport_name}")
        file.write(f"  - {iata}: {airport_name}\n")

#########################################################################################


