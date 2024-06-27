import utils
import charts
import read_csv

def run():
    country = input('Type Country: ')
    if country == 'Densidad':
        labels,values=utils.get_axes_pie()
        charts.generate_pie_chart(labels,values)
    else: 
        result = utils.get_dict_country(country)
        if len(result)>0:
            keys, values = utils.get_population(result)
            charts.generate_bar_chart(country,keys,values)
        else:
            print('Ciudad no encontrada')

if __name__=='__main__':
    run()




