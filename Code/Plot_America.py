from Libraries import *
#########################################################################################

american_countries = [
    'Antigua and Barbuda', 'Argentina', 'Bahamas', 'Barbados', 'Belize', 'Bolivia', 'Brazil', 'Canada', 'Chile',
    'Colombia', 'Costa Rica', 'Cuba', 'Dominica', 'Dominican Republic', 'Ecuador', 'El Salvador', 'Grenada',
    'Guatemala', 'Guyana', 'Haiti', 'Honduras', 'Jamaica', 'Mexico', 'Nicaragua', 'Panama', 'Paraguay', 'Peru',
    'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent and the Grenadines', 'Suriname', 'Trinidad and Tobago',
    'United States', 'Uruguay', 'Venezuela'
]

#########################################################################################

# Data Filtering
american_airports = Dataset[Dataset['country.name_x'].isin(american_countries)]

# Graph
G = nx.DiGraph()

# Add nodes to the graph with position
for index, row in american_airports.iterrows():
    G.add_node(row['IATA_x'], pos=(row['long_x'], row['lat_x']))
    G.add_node(row['IATA_y'], pos=(row['long_y'], row['lat_y']))

# Add Edges
for index, row in american_airports.iterrows():
    G.add_edge(row['IATA_x'], row['IATA_y'])

#########################################################################################
# Create plot
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

# add edges
nx.draw_networkx_edges(G, pos, edge_color='red', alpha=0.2, arrows=True, ax=ax)

# title and x y
plt.title('Flight Route Network - American Airports (outgoing Routes)')
plt.xlabel('Longitude')
plt.ylabel('Latitude')

# Save Plot
plt.savefig('american_airports_routes.png', dpi=800)
plt.close()


#########################################################################################

# Calculate the number of outgoing and incoming routes
outgoing_routes = american_airports['IATA_x'].nunique()
incoming_routes = american_airports['IATA_y'].nunique()

print(f"Numero di rotte in uscita dal continente delle americhe: {outgoing_routes}")
print(f"Numero di rotte in entrata nel continente delle americhe: {incoming_routes}")

#########################################################################################
