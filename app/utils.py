import read_csv
import re
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_dir, 'world.csv')
data = read_csv.read_csv(csv_path)

def get_dict_country(country):
    dict_country = [row for row in data if row['Country/Territory']==country]
    return dict_country

def get_population(country_dict):
    key_country= list(country_dict[0].keys())
    key_population=[i for i in key_country[5:13]]
    y_population = {year:value for year, value in country_dict[0].items() if year in key_population}
    np = [re.findall(r'\d+',n) for n in key_population]
    n_population=[element for sublist in np for element in sublist]
    d_country = {year:population for year, population in zip(n_population,y_population.values())}
    keys = d_country.keys()
    values =[int(values) for values in d_country.values()]
    return keys,values

def get_axes_pie():
    densidad_p ={row['Country/Territory']:row['World Population Percentage'] for row in data}
    keys = densidad_p.keys()
    values = [float(values) for values in densidad_p.values()]
    return keys,values

def population_by_country(data, country):
  result = list(filter(lambda i: i['Country']==country, data))
  return result