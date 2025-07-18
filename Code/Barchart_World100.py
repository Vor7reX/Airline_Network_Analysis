from Libraries import *

# i don't use this in my report but is interesting

#########################################################################################
# Calc


# Count number of routes between airport with col (IATA_x e IATA_y)
route_counts = Dataset.groupby('IATA_x').size().reset_index(name='num_routes')

# Sorting and take only the top 100 for better data visualization and also for computational time wow
sorted_routes = route_counts.sort_values(by='num_routes', ascending=False).head(100)

#########################################################################################

# Create plot
plt.figure(figsize=(12, 8))

# Plot
plt.bar(sorted_routes['IATA_x'], sorted_routes['num_routes'], color='skyblue')

# title and label
plt.xlabel('Aeroporto (IATA Code)', fontsize=12)
plt.ylabel('Numero di Rotte', fontsize=12)
plt.title('Top 100 Aeroporti per Numero di Rotte (Entrate/Uscite)', fontsize=14)
plt.xticks(rotation=90, fontsize=6)

# Save as png
plt.savefig('Top_100_Airports_by_Routes_Bar_Chart.png', dpi=300)
plt.close()

#########################################################################################

