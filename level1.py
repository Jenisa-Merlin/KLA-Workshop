import json
from PIL import Image
from collections import Counter
import csv

def load_data_json(filepath):
    with open(filepath, 'r') as f:
        data = json.load(f)
    return data

def load_image(filepath):
    img = Image.open(filepath)
    return img

def get_pixel_values(img):
    return list(img.getdata())

def find_majority_pixel(*lists, position):
    if len(set(map(len, lists))) != 1:
        return None
    
    pixels = [lst[position] for lst in lists]
    pixel_counter = Counter(pixels)
    majority_pixel = pixel_counter.most_common(1)

    if majority_pixel:
        return majority_pixel[0][0]
    else:
        return None

def compare_lists(list1,list2):
    y=[]
    for i in range(0,len(list1)):
        if(list1[i]!=list2[i]):
            y.append(i)
    return y

def get_defective_pixels(pix_vals):
    x=[]
    for i in range(0,len(pix_vals[0])):
        position = i
        err =find_majority_pixel(*pix_vals, position=position)
        x.append(err)

    err_lists = []
    for i in range(len(pix_vals)):
        err = compare_lists(x, pix_vals[i])
        err_lists.append(err)
    
    x=[]
    y=[]
    rows = []
    for i in range(len(err_lists)):
        for j in range(len(err_lists[i])):
            x1 = err_lists[i][j] % 800
            y1 = 599 - err_lists[i][j] % 600
            x.append(x1)
            y.append(y1)
            rows.append([i+1, x1, y1])
    return rows

def write_defects_csv(filename, rows):
    with open(filename, 'w') as f:
        write = csv.writer(f)
        write.writerows(rows)

if __name__ == '__main__':
    data = load_data_json("C:\\Users\\jenis\\Downloads\\KLA\\Workshop_Problem\\Level_1_Input_Data\\input.json")
    pix_vals = []
    image_paths = ["C:\\Users\\jenis\\Downloads\\KLA\\Workshop_Problem\\Level_1_Input_Data\\wafer_image_1.png","C:\\Users\\jenis\\Downloads\\KLA\\Workshop_Problem\\Level_1_Input_Data\\wafer_image_2.png","C:\\Users\\jenis\\Downloads\\KLA\\Workshop_Problem\\Level_1_Input_Data\\wafer_image_3.png","C:\\Users\\jenis\\Downloads\\KLA\\Workshop_Problem\\Level_1_Input_Data\\wafer_image_4.png","C:\\Users\\jenis\\Downloads\\KLA\\Workshop_Problem\\Level_1_Input_Data\\wafer_image_5.png"]
    for path in image_paths:
        img = load_image(path)
        pix_vals.append(get_pixel_values(img))
    
    rows = get_defective_pixels(pix_vals)
    write_defects_csv('defects', rows)
