import os
import csv
import numpy as np

map = {
    1 : {
        'High' : 0,
        'Moderate' : 1,
        'Low' : 2
    }, 
    2 : {
        'Expensive' : 0, 
        'Normal' : 1,
        'Cheap' : 2
    }, 
    3 : {
        'Loud' : 0,
        'Quiet' : 1
    }, 
    4 : {
        'Talpiot' : 0,
        'City-Center' : 1,
        'German-Colony' : 2,
        'Ein-Karem' : 3,
        'Mahane-Yehuda' : 4
    }, 
    5 : {
        'No' : 0,
        'Yes' : 1
    },
    6 : {
        'No' : 0,
        'Yes' : 1
    },
    7 : {
        'No' : 'N',
        'Yes' : 'Y'
    }
}


def gene_dataset():
    csv_path = os.getcwd()

    csv_filename = csv_path + '/quantify_dataset.csv'
    if os.path.exists(csv_filename): 
        os.remove(csv_filename)
    csv_handle = open(csv_filename, "wb+")
    writer = csv.writer(csv_handle)

    with open('dt-data.txt') as txt_file:
        line = txt_file.readline()
        line = txt_file.readline()

        line_num = 0
        while line:
            arr = line.split(' ')
            if len(arr) < 8 : 
                continue
            rowdata = []
            for index in range(1, len(arr)):
                element = arr[index].replace(',', '').replace(';', '').replace(' ', '')
                for key in map[index].keys():
                    if key == element.strip():
                        rowdata.append(map[index][key])
            writer.writerow(rowdata)
            line = txt_file.readline()

    csv_handle.close()

    #dataset = [line.split(',') for line in open('quantify_dataset.csv')]
    data = np.loadtxt('quantify_dataset.csv',delimiter=',',dtype='str')
    features = data[:,:-1].astype('int').tolist()
    labels = data[:,-1:].tolist()
    for i in range(len(features)):
        features[i].append(labels[i][0])
    dataset = features

    features = ['Occupied', 'Price', 'Music', 'Location', 'VIP', 'Favorite Beer'] 

    return dataset, features

def get_featval():
    map = {
        'Occupied' : {
            'High' : 0,
            'Moderate' : 1,
            'Low' : 2
        }, 
        'Price' : {
            'Expensive' : 0, 
            'Normal' : 1,
            'Cheap' : 2
        }, 
        'Music' : {
            'Loud' : 0,
            'Quiet' : 1
        }, 
        'Location' : {
            'Talpiot' : 0,
            'City-Center' : 1,
            'German-Colony' : 2,
            'Ein-Karem' : 3,
            'Mahane-Yehuda' : 4
        }, 
        'VIP' : {
            'No' : 0,
            'Yes' : 1
        },
        'Favorite Beer' : {
            'No' : 0,
            'Yes' : 1
        },
        'Enjoy' : {
            'No' : 0,
            'Yes' : 1
        }
    }
    return map

def main():
    dataset, features = gene_dataset()


if __name__ == "__main__":
    main()