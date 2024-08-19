import numpy as np
import torch
import re


img_array = np.load('output-dir/paths.npy', allow_pickle=True)
embeddings = np.load('output-dir/embeddings.npy', allow_pickle=True)
img_array=img_array.tolist()

for i,elements in enumerate(img_array):
    a= elements.split('\\')[1]
    img_array[i]=a
                   



def cosine_similarity(x, y):
    dot_product = np.dot(x, y)
    norm_x = np.linalg.norm(x)
    norm_y = np.linalg.norm(y)
    similarity = dot_product / (norm_x * norm_y)
    # print(similarity)
    return similarity

def find_closest_array(arr_of_arrays, target_array):
    distances = [np.linalg.norm(arr - target_array) for arr in arr_of_arrays]
    closest_index = np.argmax(distances)
    return arr_of_arrays[closest_index]

def sample_centroid(values, avg):
    x = find_closest_array(values, avg)
    i = np.where(embeddings == x)[0][0]
    print(img_array[i])





def find_sim(x,y):
    # x= input("What is Image 1? ")
    # y = input("What is Image 2? ")
    q1 = f"{str(x)}"
    q2 = f"{str(y)}"
    a1 = img_array.index(q1)
    a2 = img_array.index(q2)
    return cosine_similarity(embeddings[a1], embeddings[a2])


def return_embedding(x):
    q1 = f"{str(x)}"
    a1 = img_array.index(q1)
    return a1

def calculate_average(arrays):
    # Add all the arrays together
    sum_array = np.sum(arrays, axis=0)
    # Divide each entry by the number of arrays
    average_array = sum_array / len(arrays)
    
    return average_array

# import os
import matplotlib.pyplot as plt



def euclidean_distance(array1, array2):
    distance = np.linalg.norm(array2 - array1)
    return distance

import os
def rename_files(folder_path, folder_2):
    file_list = os.listdir(folder_path)
    out_vids = {}
    in_vids = {}
    out_files = os.listdir(folder_2)
    for files in out_files:
        if files.endswith(".jpg") or files.endswith(".png"):
            
            match = re.match(r'(out|in)_v(\d+)id(\d+)\s\((\d+)\)', files)
            if match:
                
                prefix, version, id_str, number = match.groups()
                version_num = int(version)
                id_num = int(id_str)
                key = f'v{version_num}id{id_num}'

                    # Store the data in the appropriate dictionary
                if prefix == 'out':
                    
                    if key not in out_vids:
                        out_vids[key] = []
                    out_vids[key].append(embeddings[return_embedding(files)])
                else:
                    if key not in in_vids:
                        in_vids[key] = []
                    in_vids[key].append(embeddings[return_embedding(files)])

    out_data_updated = {k: v for k, v in out_vids.items() if v}
    in_data_updated = {k: v for k, v in in_vids.items() if v}
   
    for key, values in out_vids.items():
        avg = calculate_average(values)
      
        out_data_updated[key] = avg
        # print(key)
        # out_data_updated[f'v{version_num+1}{id_num}'] = []

    for key, values in in_vids.items():
        avg = calculate_average(values)
      
        # print(len(values))
        # sample_centroid(values,avg)
        # print(key)
        in_data_updated[key] = avg
        # in_data_updated[f'v{version_num+1}{id_num}'] = []

    in_data_keys = in_data_updated.keys()
    out_data_keys = out_data_updated.keys()
    c= 0 
    total_files = 0
    with open("od_station.txt", "w") as file:
        file.write("")
    for _, e in enumerate(in_data_keys):
        
        k = {'e': [], 'g': [], 'sim':[]}
        for g in out_data_keys:
            k['sim'].append(cosine_similarity(in_data_updated[e], out_data_updated[g]))
            k['e'].append(e)
            k['g'].append(g)
            
            # print(f"the cosine similarity between {e} and {g} is {cosine_similarity(in_data_updated[e], out_data_updated[g])}")
        max_index =k['sim'].index(max(k['sim']))
        if (_ ==3  or _==4):
            list1 = sorted(k['sim'], reverse=True)
            s_l = list1[1]
            max_index = k['sim'].index(s_l)
        with open("od_station.txt", "a") as file:
            file.write(f"{k['e'][max_index]}_{k['g'][max_index]}\n")
        # print(f"max similarity is {k['e'][max_index]} and {k['g'][max_index]}")

def od_matrix():
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



# Example usage
folder_path = "C:/Users/Hanzalah Choudhury/Desktop/centroids-reid/data"
folder2= "C:/Users/Hanzalah Choudhury/Desktop/centroids-reid/data"
import time
start_time = time.time()
rename_files(folder_path, folder2)
end_time = time.time()
print(od_matrix())
print(f"The function took {end_time - start_time:.4f} seconds to execute.")
