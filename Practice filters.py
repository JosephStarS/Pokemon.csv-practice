import pandas as pd
import sqlite3 as sql

df = pd.read_csv('pokemon_cleaned.csv')

print(df.head())
#“I’m loading the cleaned dataset to verify that the transformations were applied correctly and to prepare for further analysis.”

# Filter Pokémon with Total greater than 500
strong_pokemon = df[df['Total'] > 500]
print(strong_pokemon)
#“I’m filtering the dataset to find Pokémon with a Total stat greater than 500, which allows me to focus on the stronger Pokémon for analysis or
#  comparison.”

# Filter Pokémon of type 'fire'
fire_pokemon = df[df['Type 1'] == 'fire']
print(fire_pokemon)
#“I’m filtering the dataset to find Pokémon of the 'fire' type, which helps me analyze or compare characteristics specific to that type.”

legendary_df = df[(df['Legendary'] == True) & (df['Total'] > 600)]
legendary_df[['Name', 'Total', 'Type 1']]
print(legendary_df[['Name', 'Total', 'Type 1']])
#“I’m filtering the dataset to find legendary Pokémon with a Total stat greater than 600, and then selecting only the 'Name', 'Total',
#  and 'Type 1' columns for a focused view of these powerful Pokémon.”

# Agrupar por tipo y calcular el promedio de HP
avg_hp = df.groupby('Type 1')['HP'].mean().reset_index()

# Orden ascendente (de menor a mayor HP)
avg_hp_asc = avg_hp.sort_values(by='HP', ascending=True)
print("Orden ascendente (menor HP promedio):")
print(avg_hp_asc)

# Orden descendente (de mayor a menor HP)
avg_hp_desc = avg_hp.sort_values(by='HP', ascending=False)
print("\nOrden descendente (mayor HP promedio):")
print(avg_hp_desc)

print("Pokémon con HP menor a 100")
low_hp = df[df['HP'] < 100]
#“Estoy filtrando el DataFrame para encontrar Pokémon con HP menor a 100, lo que me permite identificar a los Pokémon más débiles en 
# términos de HP para análisis o comparación.”

#  Orden descendente (los más cercanos a 100 primero)
low_hp_asc = low_hp.sort_values(by='HP', ascending=False)
print("Orden descendente (los más cercanos a 100 primero)")
print(low_hp_asc.head(20)[['Name', 'HP', 'Type 1']])

#  Orden ascendente (los más débiles primero)
low_hp_desc = low_hp.sort_values(by='HP', ascending=True)
print("Orden ascendente (los más débiles primero)")
print(low_hp_desc.head(20)[['Name', 'HP', 'Type 1']])

# Clasificar Pokémon por nivel de fuerza

def categorize_strength(total):
    if total >= 600:
        return 'Strong'
    elif total >= 400:
        return 'Average'
    else:
        return 'Weak'

df['Strength'] = df['Total'].apply(categorize_strength)
print(df[['Name', 'Total', 'Strength']])


df['Category'] = pd.cut(pd.to_numeric(df['Total'], errors='coerce'),
                        bins=[0, 400, 600, 800],
                        labels=['Weak', 'Average', 'Strong'])

#“I’m defining a function to categorize Pokémon strength based on their Total stat, and then applying this function to 
# create a new 'Strength' column in the DataFrame for easier classification.”


# Encuentra el tipo con el mayor promedio de ataque
avg_attack = df.groupby('Type 1')['Attack'].mean().reset_index()
top_type = avg_attack.sort_values(by='Attack', ascending=False).head(1)
print(top_type) 


# Escalar valores de HP entre 0 y 1
df['HP_normalized'] = (pd.to_numeric(df['HP'], errors='coerce') - df['HP'].min()) / (df['HP'].max() - df['HP'].min())

def adjust_attack(value):
    if value > 100:
        return value * 1.1  # Aumenta 10% si es alto
    else:
        return value

df['Adjusted_Attack'] = df['Attack'].apply(adjust_attack)
#“I’m normalizing the HP values to a 0-1 scale for better comparison, and then defining a function to adjust the Attack stat by increasing 
# it by 10% if it’s greater than 100, which allows for a more nuanced analysis of Pokémon strength.”


# Combinar tipo principal y secundario
df['Type_Combined'] = df['Type 1'] + '/' + df['Type 2']

# Renombrar columnas para mayor claridad
df.rename(columns={'Sp. Atk': 'Special_Attack', 'Sp. Def': 'Special_Defense'}, inplace=True)

# Reordenar columnas para presentación
df = df[['Name', 'Type 1', 'Type 2', 'HP', 'Attack', 'Defense', 'Total']]

# Calcular promedio y máximo de HP por tipo
stats = df.groupby('Type 1')['HP'].agg(['mean', 'max']).reset_index()
print(stats)

# Calcular promedio y máximo de HP por tipo
stats = df.groupby('Type 1')['HP'].agg(['mean', 'max']).reset_index()
print(stats)

# Renombrar columnas para mayor claridad
df.rename(columns={'Sp. Atk': 'Special_Attack', 'Sp. Def': 'Special_Defense'}, inplace=True)

# Clasificar Pokémon por nivel de fuerza
df['Category'] = pd.cut(df['Total'], bins=[0, 400, 600, 800], labels=['Weak', 'Average', 'Strong'])