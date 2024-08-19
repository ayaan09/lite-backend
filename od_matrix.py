import matplotlib.pyplot as plt
import json

import sys

#file1 = h.txt; file2 = file.txt
def od_matrix(file1, file2):

    enter_=[]
    exit_=[]
    with open(file1) as f:
        d = json.load(f)


    for path, data in d.items():
        enter = data['Enter']
        ex = data['Exit']
        enter_.append(int(enter[5:]))
        exit_.append(int(ex[5:]))
    n = len(enter_)
    od = [[0] * n for _ in range(n)]
    # Load the JSON data from the file
    with open(file2) as file:
        data = json.load(file)
    ent=[]
    exit=[]
    # Iterate through each entry in the data
    for image_path, image_data in data.items():
        frames = image_data['paths']
        ent.append(int(image_path.split('\\')[1].split("_")[0][5:]))
        exit.append(int(frames[1].split("\\")[2].split("_")[0][5:]))

    for i in range(len(ent)):
        for j in range(len(enter_)):
            if(ent[i]>= enter_[j] and ent[i]< exit_[j]):
                ent[i] = j
                
            if(exit[i]>= enter_[j] and exit[i]< exit_[j]):
                exit[i] = j
    for i in range(len(ent)):  
 
        a= ent[i]
        b=exit[i]
        od[a][b]+=1

                        


 
    print(od)

def read_od():
    with open("od_station.txt", "r") as file:
        f = file.readlines()
    od_matrix_4 = [[0,0,0,0],[0,0,0,0],[0,0,0,0], [0,0,0,0]]
    for l in f:
        geo = l.split("_")
        n1 = int(geo[0][1])
        n2 = int(geo[1][1])
        od_matrix_4[n2-1][n1-1]+=1
        # print(n1,n2)
    return od_matrix_4

if __name__ == '__main__':
    read_od()
    # if len(sys.argv) < 3:
    #     print('Usage: python od_matrix.py <file1> <file2>')
    #     sys.exit(1)

    # file1_path = sys.argv[1]
    # file2_path = sys.argv[2]
    # od_matrix(file1_path, file2_path)