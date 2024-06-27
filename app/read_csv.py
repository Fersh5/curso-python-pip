import csv
import os

def read_csv(phat):
    with open(phat,'r') as csvfile:
        world=csv.reader(csvfile, delimiter=',')
        header=next(world)
        dict_list= [{header[i]:row[i] for i in range(len(header))}for row in world]
        return dict_list

if __name__=='__main__':
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(current_dir, 'world.csv')
    data = read_csv(csv_path)
    print(data)

