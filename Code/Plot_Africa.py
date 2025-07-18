from Libraries import *
#########################################################################################

african_countries = [
    'Algeria', 'Angola', 'Benin', 'Botswana', 'Burkina Faso', 'Burundi', 'Cabo Verde', 'Cameroon', 'Central African Republic',
    'Chad', 'Comoros', 'Congo', 'Democratic Republic of the Congo', 'Djibouti', 'Egypt', 'Equatorial Guinea', 'Eritrea',
    'Eswatini', 'Ethiopia', 'Gabon', 'Gambia', 'Ghana', 'Guinea', 'Guinea-Bissau', 'Ivory Coast', 'Kenya', 'Lesotho',
    'Liberia', 'Libya', 'Madagascar', 'Malawi', 'Mali', 'Mauritania', 'Mauritius', 'Morocco', 'Mozambique', 'Namibia',
    'Niger', 'Nigeria', 'Rwanda', 'São Tomé and Príncipe', 'Senegal', 'Seychelles', 'Sierra Leone', 'Somalia', 'South Africa',
    'South Sudan', 'Sudan', 'Togo', 'Tunisia', 'Uganda', 'Zambia', 'Zimbabwe'
]

#########################################################################################

# Data Filtering
african_airports = Dataset[Dataset['country.name_x'].isin(african_countries)]

# Create a graph
G_outgoing = nx.DiGraph()

# Add nodes to the graph with position
for index, row in african_airports.iterrows():
    G_outgoing.add_node(row['IATA_x'], pos=(row['long_x'], row['lat_x']))
    G_outgoing.add_node(row['IATA_y'], pos=(row['long_y'], row['lat_y']))

# Add edges
for index, row in african_airports.iterrows():
    G_outgoing.add_edge(row['IATA_x'], row['IATA_y'])

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
pos_outgoing = nx.get_node_attributes(G_outgoing, 'pos')

# Add nodes
nx.draw_networkx_nodes(G_outgoing, pos_outgoing, node_size=100, node_color='#023e8a', alpha=0.7, ax=ax)

# Add edges outgoing routes
nx.draw_networkx_edges(G_outgoing, pos_outgoing, edge_color='#FFA500', alpha=0.5, arrows=True, ax=ax)

# Title and x y labels
plt.title('Flight Route Network - Africa Airports (outgoing Routes)')
plt.xlabel('Longitude')
plt.ylabel('Latitude')

# Save Plot for outgoing routes
plt.savefig('african_airports_routes.png', dpi=800)
plt.close()

#########################################################################################

# Calculate the number of outgoing and incoming routes
outgoing_routes = african_airports['IATA_x'].nunique()
incoming_routes = african_airports['IATA_y'].nunique()

print(f"Numero di rotte in uscita dal continente Africa: {outgoing_routes}")
print(f"Numero di rotte in entrata nel continente Africa: {incoming_routes}")

#########################################################################################

