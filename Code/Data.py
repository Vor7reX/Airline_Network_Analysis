# Import Library
from Libraries import *

#########################################################################################
#########################################################################################
# DEFINIRE PATH DATSET QUI #

# Define Path CSV
routes_path = "C:/Users/hadda/Desktop/Dataset/routes.csv"
airlines_path = "C:/Users/hadda/Desktop/Dataset/airlines.csv"
airports_path = "C:/Users/hadda/Desktop/Dataset/airports-extended.csv"
#########################################################################################
#########################################################################################

# Load CSV
airlines = pd.read_csv(airlines_path)
routes = pd.read_csv(routes_path)
airports = pd.read_csv(airports_path)

#########################################################################################

# routes.csv
# Pre-elaborazione dei dati

# Sostituisco '\\N' con NaN e rimuovo le righe con valori mancanti DATA cleaning
routes.replace('\\N', np.nan, inplace=True)
routes.dropna(axis=0, how='any', inplace=True)

# Converto 'airline ID' in tipo int
routes['airline ID'] = routes['airline ID'].astype(int)

#########################################################################################

# airports-extended.csv
# Pre-elaborazione dei dati

#Data Enrichment

# Inserisco Identificazione per le collone del Dataset airports-extended per poter lavorare con il db
new_column_names = [
    'id', 'airport.name', 'city.name', 'country.name', 'IATA', 'ICAO',
    'lat', 'long', 'altitude', 'tz.offset', 'DST', 'tz.name',
    'airport.type', 'source.data'
]
airports.columns = new_column_names

#########################################################################################

#Data Aggregation
# Merge delle informazioni sui voli con le compagnie aeree -- Left Join

# Unisco il dataset routes con airlines per ottenere più informazioni sulle compagnie aeree
Dataset = pd.merge(routes, airlines, left_on='airline ID', right_on='Airline ID', how='left')

# Rimuovo spazi extra nei nomi delle colonne
Dataset.columns = Dataset.columns.str.strip()

# Correggo gli errori di battitura nei nomi delle colonne
Dataset.rename(columns={'destination apirport': 'destination airport'}, inplace=True)

# Seleziono solo le colonne di interesse per la ricerca
columns_to_keep = [
    'airline', 'airline ID', 'Name', 'Country',
    'source airport', 'source airport id',
    'destination airport', 'destination airport id',
    'codeshare', 'stops', 'equipment', 'Active'
]
Dataset = Dataset[columns_to_keep]

#########################################################################################

#Data Aggregation
# Aggiungo informazioni sui dettagli geolocalizazzione per gli aeroporti di partenza e destinazione

# Unisco il dataset con le informazioni degli aeroporti di partenza e di destinazione -- Left Join
Dataset = (
    pd.merge(Dataset, airports, left_on='source airport', right_on='IATA', how='left')
    .merge(airports, left_on='destination airport', right_on='IATA', how='left', suffixes=('_source', '_destination'))
)

# Rinomino le colonne per avere in chiaro le informazioni per i plot
Dataset.rename(columns={
    'airport.name_source': 'airport.name_x',
    'city.name_source': 'city.name_x',
    'country.name_source': 'country.name_x',
    'lat_source': 'lat_x',
    'long_source': 'long_x',
    'airport.name_destination': 'airport.name_y',
    'city.name_destination': 'city.name_y',
    'country.name_destination': 'country.name_y',
    'lat_destination': 'lat_y',
    'long_destination': 'long_y',
    'source airport id': 'source airport id_x',
    'destination airport id': 'destination airport id_y',
    'IATA_source': 'IATA_x',
    'IATA_destination': 'IATA_y',
    'Name': 'Company_Name'
}, inplace=True)

#########################################################################################


# Colonne finali da mantenere per il dataset finale
final_columns = [
    'Company_Name',
    'Country',
    'city.name_x',
    'country.name_x',
    'airport.name_x',
    'IATA_x',
    'lat_x', 'long_x',
    'city.name_y',
    'country.name_y',
    'airport.name_y',
    'IATA_y',
    'lat_y', 'long_y',
    'source airport id_x',
    'destination airport id_y'
]

Dataset = Dataset[final_columns]

# Stampo le prime 5 righe del dataset for debug
print(Dataset.head(5).to_string(index=False))



#########################################################################################
#########################################################################################
# DEFINIRE PATH DATSET QUI #
# Salvo il DataFrame in un file CSV

output_path = "C:/Users/hadda/Desktop/Dataset/Dataset_airlines.csv"
Dataset.to_csv(output_path, index=False)
print(f"File CSV 'Dataset_airlines.csv' salvato con successo! in {output_path}.")

#########################################################################################
#########################################################################################


