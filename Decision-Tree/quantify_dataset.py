import os
import csv


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
        'No' : 0,
        'Yes' : 1
    }
}



csv_path = os.getcwd()
csv_filename = csv_path + '/quantify_dataset.csv'
csv_handle = open(csv_filename, "wb+")
writer = csv.writer(csv_handle)

with open('dataset/dt-data.txt') as txt_file:
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