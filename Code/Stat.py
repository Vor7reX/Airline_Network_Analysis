from Libraries import *
#########################################################################################

# Calc stats
num_total_routes = len(Dataset)
num_unique_airports_x = Dataset['IATA_x'].nunique()
num_unique_airports_y = Dataset['IATA_y'].nunique()
num_unique_airports = len(set(Dataset['IATA_x']).union(set(Dataset['IATA_y'])))
num_countries = Dataset['Country'].nunique()
num_companies = Dataset['Company_Name'].nunique()
#########################################################################################

# Result
results = {
    "Numero totale di rotte": num_total_routes,
    "Numero totale di aeroporti unici": num_unique_airports,
    "Numero di aeroporti unici di partenza": num_unique_airports_x,
    "Numero di aeroporti unici di arrivo": num_unique_airports_y,
    "Numero di paesi coinvolti": num_countries,
    "Numero di compagnie aeree uniche": num_companies
}
#########################################################################################

# Print
for key, value in results.items():
    print(f"{key}: {value}")
