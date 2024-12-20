import os
import shutil

path = input("Enter the path you want to sort") + "\\"
files = os.listdir(path)
folders = ['pdf', 'csv', 'img','text']
counter = 0

for x in range(0,4):
    if not os.path.exists(path + folders[x]):
        os.makedirs(path+folders[x])

for y in files:
    if ".pdf" in y and not os.path.exists(path+"pdf\\" + y):
        shutil.move(path+y, path + "pdf\\" + y)
        counter += 1
    elif ".csv" in y and not os.path.exists(path+"csv\\" + y):
        shutil.move(path+y, path + "csv\\" + y)
        counter += 1
    elif ".png" in y and not os.path.exists(path+"img\\" + y):
        shutil.move(path+y, path + "img\\" + y)
        counter += 1
    elif ".txt" in y and not os.path.exists(path+"text\\" + y):
        shutil.move(path+y, path + "text\\" + y)
        counter += 1
    elif ".jpeg" in y and not os.path.exists(path+"img\\" + y):
        shutil.move(path+y, path + "img\\" + y)
        counter += 1

if counter == 0:
    print("no files were moved")
    