import utils
import read_csv

def run():
    country = input('Type Country: ')
    result = utils.get_dict_country(country)
    if len(result)>0:
        keys, values = utils.get_population(result)
    print(keys,values)

if __name__=='__main__':
    run()




