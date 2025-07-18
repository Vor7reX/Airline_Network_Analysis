from Libraries import *
#########################################################################################

oceania_countries = [
    'Australia', 'Fiji', 'Kiribati', 'Marshall Islands', 'Micronesia', 'Nauru', 'New Zealand', 'Palau', 'Papua New Guinea',
    'Samoa', 'Solomon Islands', 'Tonga', 'Tuvalu', 'Vanuatu'
]

#########################################################################################
# Data Filtering
oceania_airports = Dataset[Dataset['country.name_x'].isin(oceania_countries)]

# Graph
G = nx.DiGraph()

# Add nodes to the graph with the position
for index, row in oceania_airports.iterrows():
    G.add_node(row['IATA_x'], pos=(row['long_x'], row['lat_x']))
    G.add_node(row['IATA_y'], pos=(row['long_y'], row['lat_y']))

# Add Edges(only routs out the Oceania Continente)
for index, row in oceania_airports.iterrows():
    G.add_edge(row['IATA_x'], row['IATA_y'])

# create plot
plt.figure(figsize=(20, 16))
ax = plt.axes(projection=ccrs.PlateCarree())

# Graphics Elements for cartopy
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=':')
ax.add_feature(cfeature.LAND, color='#f8f1e4')
ax.gridlines(draw_labels=True, color='#f8f1e4', linestyle='--', alpha=0.5)

# Position nodes
pos = nx.get_node_attributes(G, 'pos')

# add nodes
nx.draw_networkx_nodes(G, pos, node_size=100, node_color='#023e8a', alpha=0.7, ax=ax)

# add edges
nx.draw_networkx_edges(G, pos, edge_color='#66CDAA', alpha=0.3, arrows=True, ax=ax)

# title and x y
plt.title('Flight Route Network - Oceania Airports (outgoing Routes)')
plt.xlabel('Longitude')
plt.ylabel('Latitude')

# Save Plot
plt.savefig('oceania_airports_routes.png', dpi=800)
plt.close()
#########################################################################################

# Calc number of outgoing and incoming routes
outgoing_routes = oceania_airports['IATA_x'].nunique()
incoming_routes = oceania_airports['IATA_y'].nunique()

print(f"Numero di rotte in uscita dal continente Oceania: {outgoing_routes}")
print(f"Numero di rotte in entrata nel continente Oceania: {incoming_routes}")
