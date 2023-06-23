import json
with open("C:\\Users\\jenis\\Downloads\\KLA\\Workshop_Problem\\Level_1_Input_Data\\input.json", 'r') as f:
  data = json.load(f)
print(data)

from PIL import Image
img1 = Image.open("C:\\Users\\jenis\\Downloads\\KLA\\Workshop_Problem\\Level_1_Input_Data\\wafer_image_1.png")
#img1.show()

img2 = Image.open("C:\\Users\\jenis\\Downloads\\KLA\\Workshop_Problem\\Level_1_Input_Data\\wafer_image_2.png")
#img2.show()

img3 = Image.open("C:\\Users\\jenis\\Downloads\\KLA\\Workshop_Problem\\Level_1_Input_Data\\wafer_image_3.png")
#img3.show()

img4 = Image.open("C:\\Users\\jenis\\Downloads\\KLA\\Workshop_Problem\\Level_1_Input_Data\\wafer_image_4.png")
#img4.show()

img5 = Image.open("C:\\Users\\jenis\\Downloads\\KLA\\Workshop_Problem\\Level_1_Input_Data\\wafer_image_5.png")
#img5.show()

from collections import Counter

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

pix_val1 = list(img1.getdata())
pix_val2 = list(img2.getdata())
pix_val3 = list(img3.getdata())
pix_val4 = list(img4.getdata())
pix_val5 = list(img5.getdata())

x=[]
for i in range(0,len(pix_val1)):
    position = i
    err =find_majority_pixel(pix_val1,pix_val2,pix_val3,pix_val4,pix_val5,position=position)
    x.append(err)

err1 = compare_lists(x,pix_val1)
err2 = compare_lists(x,pix_val2)
err3 = compare_lists(x,pix_val3)
err4 = compare_lists(x,pix_val4)
err5 = compare_lists(x,pix_val5)

x=[]
y=[]
for i in range(len(err1)):
    x1 = err1[i]%800
    y1= err1[i]%600
    x.append(x1)
    y.append(y1)
rows =[]
for i in range(0,len(x)):
    rows.append([1,x[i],y[i]])

for i in range(len(err2)):
    x1 = err2[i] % 800
    y1 = err2[i] % 600
    x.append(x1)
    y.append(y1)
for i in range(0,len(x)):
    rows.append([2,x[i],y[i]])

for i in range(len(err3)):
    x1 = err3[i] % 800
    y1 = err3[i] % 600
    x.append(x1)
    y.append(y1)
for i in range(0,len(x)):
    rows.append([3,x[i],y[i]])

for i in range(len(err4)):
    x1 = err4[i] % 800
    y1 = err4[i] % 600
    x.append(x1)
    y.append(y1)
for i in range(0,len(x)):
    rows.append([4,x[i],y[i]])

for i in range(len(err5)):
    x1 = err5[i] % 800
    y1 = err5[i] % 600
    x.append(x1)
    y.append(y1)
for i in range(len(err5)):
    rows.append([5,x[i],y[i]])

print(rows)

import csv
with open('defects', 'w') as f:
    write = csv.writer(f)
    write.writerows(rows)

