import read_csv
import re

data = read_csv.read_csv('./world_population.csv')

mex= [row for row in data if row['Country/Territory']=='Mexico']
t_key=list(mex[0].keys())
p_key= [i for i in t_key[5:13]]
pop_mex = {key:value for key,value in mex[0].items() if key in p_key}
np_key = [re.findall(r'\d+',n) for n in p_key]
# np_keyf=[]
# for sublista in np_key:
#     for elemento in sublista:
#         np_keyf.append(elemento)
np_keyf = [elemento for sublista in np_key for elemento in sublista]
mex_pf={key:valor for key,valor in zip(np_keyf,pop_mex.values())}

# '---------------------------------------------------------------------------------

densidad_p ={row['Country/Territory']:row['World Population Percentage'] for row in data}
keys = densidad_p.keys()
values = [float(values) for values in densidad_p.values()]
print(values)
#-----------------------------------------------------------------------------------

