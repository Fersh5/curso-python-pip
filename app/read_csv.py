import csv

def read_csv(phat):
    with open(phat,'r') as csvfile:
        world=csv.reader(csvfile, delimiter=',')
        header=next(world)
        dict_list= [{header[i]:row[i] for i in range(len(header))}for row in world]
        return dict_list

if __name__=='__main__':
    data = read_csv('./world_population.csv')
    print(data)

