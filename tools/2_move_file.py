import os
import shutil

path = './files'
files = os.listdir(path)

for f in files:
    folder_name = './files/' + f.split('.')[-1]
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        shutil.move(f, folder_name)
    else:
        shutil.move(f, folder_name)