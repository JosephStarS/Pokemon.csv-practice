import pandas as pd

df = pd.read_csv('pokemon.csv')
df.head()
df.info()
df.describe()

#“I’m loading the dataset with Pandas, 
# checking the first few rows, and inspecting column types to understand the structure before transforming anything.”

df.drop_duplicates(inplace=True)
#“I’m removing duplicate entries to ensure data quality and avoid skewing analysis results.”

# Limpiar valores nulos
df.fillna({
    'Type 2': 'None',       # Reemplaza nulos en Type 2 por 'None'
    'HP': 'No data',        # Sustituye nulos en HP por 'No data'
    'Attack': 0,            # Sustituye nulos en Attack por 0
    'Defense': 0            # Sustituye nulos en Defense por 0
}, inplace=True)

# Verificar limpieza
print(df.isnull().sum())

# Estandarizar texto
df['Type 1'] = df['Type 1'].str.lower().str.strip()
df['Name'] = df['Name'].str.title().str.strip()

# Convertir columnas numéricas (excepto HP, que tiene texto)
numeric_cols = ['Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')

# Estandarizar texto
df['Type 1'] = df['Type 1'].str.lower().str.strip()
df['Name'] = df['Name'].str.title().str.strip()

# Convertir columnas numéricas (excepto HP, que tiene texto)
numeric_cols = ['Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')


df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
#“I’m creating a new 'Total' column by summing the relevant stats to have a comprehensive measure of each Pokémon's overall strength for easier comparison.”    

df_types = df[['Name', 'Type 1']]
df_stats = df[['Name', 'Total']]
merged_df = pd.merge(df_types, df_stats, on='Name')
print(merged_df)
#“I’m merging the 'Name' and 'Type 1' columns with the 'Name' and 'Total' columns to create a new DataFrame that combines type and total stats 
# for easier analysis.”


df.to_csv('pokemon_cleaned.csv', index=False)
#“I’m saving the cleaned dataset to a new CSV file without the index to keep it tidy and ready for further analysis or sharing.”

#“¿Qué pasa si hay valores nulos en HP?”  
# “Podría usar df['HP'].fillna(df['HP'].mean()) o dropna() dependiendo del contexto del pipeline.”