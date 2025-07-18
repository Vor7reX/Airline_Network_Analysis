from Libraries import *
#########################################################################################

european_countries = [
    'Albania', 'Andorra', 'Armenia', 'Austria', 'Azerbaijan', 'Belarus', 'Belgium', 'Bosnia and Herzegovina',
    'Bulgaria', 'Croatia', 'Cyprus', 'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France', 'Georgia',
    'Germany', 'Greece', 'Hungary', 'Iceland', 'Ireland', 'Italy', 'Kazakhstan', 'Kosovo', 'Latvia', 'Liechtenstein',
    'Lithuania', 'Luxembourg', 'Malta', 'Moldova', 'Monaco', 'Montenegro', 'Netherlands', 'North Macedonia', 'Norway',
    'Poland', 'Portugal', 'Romania', 'Russia', 'San Marino', 'Serbia', 'Slovakia', 'Slovenia', 'Spain', 'Sweden',
    'Switzerland', 'Turkey', 'Ukraine', 'United Kingdom', 'Vatican City'
]

#########################################################################################
# Data Filtering
european_airports = Dataset[Dataset['country.name_x'].isin(european_countries)]

# Graph
G = nx.DiGraph()

# Add nodes to the graphd with the position
for index, row in european_airports.iterrows():
    G.add_node(row['IATA_x'], pos=(row['long_x'], row['lat_x']))
    G.add_node(row['IATA_y'], pos=(row['long_y'], row['lat_y']))

# Add Edges(only routes out Europa Continente)
for index, row in european_airports.iterrows():
    G.add_edge(row['IATA_x'], row['IATA_y'])

#create plot
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
nx.draw_networkx_edges(G, pos, edge_color='#FFDD00', alpha=0.3, arrows=True, ax=ax)

# title and x y
plt.title('Flight Route Network - Europe Airports (outgoing Routes)')
plt.xlabel('Longitude')
plt.ylabel('Latitude')

# Save Plot
plt.savefig('european_airports_routes.png', dpi=800)
plt.close()
#########################################################################################

# Calc the number of outgoing and incoming routes
outgoing_routes = european_airports['IATA_x'].nunique()
incoming_routes = european_airports['IATA_y'].nunique()

print(f"Numero di rotte in uscita dal continente Europa: {outgoing_routes}")
print(f"Numero di rotte in entrata nel continente Europa: {incoming_routes}")

#########################################################################################
