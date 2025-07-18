from Libraries import *
#########################################################################################

asian_countries = [
    'Afghanistan', 'Armenia', 'Azerbaijan', 'Bahrain', 'Bangladesh', 'Bhutan', 'Brunei', 'Cambodia', 'China', 'Cyprus',
    'Georgia', 'India', 'Indon  esia', 'Iran', 'Iraq', 'Israel', 'Japan', 'Jordan', 'Kazakhstan', 'Korea, North',
    'Korea, South', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Lebanon', 'Malaysia', 'Maldives', 'Mongolia', 'Myanmar', 'Nepal',
    'Oman', 'Pakistan', 'Palestine', 'Philippines', 'Qatar', 'Russia', 'Saudi Arabia', 'Singapore', 'Sri Lanka', 'Syria',
    'Tajikistan', 'Thailand', 'Timor-Leste', 'Turkey', 'Turkmenistan', 'United Arab Emirates', 'Uzbekistan', 'Vietnam',
    'Yemen'
]

#########################################################################################
# Data Filtering
asian_airports = Dataset[Dataset['country.name_x'].isin(asian_countries)]

# Graph
G = nx.DiGraph()

# Add nodes to the graph with the position
for index, row in asian_airports.iterrows():
    G.add_node(row['IATA_x'], pos=(row['long_x'], row['lat_x']))
    G.add_node(row['IATA_y'], pos=(row['long_y'], row['lat_y']))

# Add Edges
for index, row in asian_airports.iterrows():
    G.add_edge(row['IATA_x'], row['IATA_y'])
#########################################################################################

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
nx.draw_networkx_edges(G, pos, edge_color='#1E90FF', alpha=0.3, arrows=True, ax=ax)

# title and x y
plt.title('Flight Route Network - Asian Airports (outgoing Routes)')
plt.xlabel('Longitude')
plt.ylabel('Latitude')

# Save Plot
plt.savefig('asian_airports_routes.png', dpi=800)
plt.close()
#########################################################################################

# Calc the number of outgoing and incoming routes
outgoing_routes = asian_airports['IATA_x'].nunique()
incoming_routes = asian_airports['IATA_y'].nunique()

print(f"Numero di rotte in uscita dal continente Asiatico: {outgoing_routes}")
print(f"Numero di rotte in entrata nel continente Asiatico: {incoming_routes}")

#########################################################################################

