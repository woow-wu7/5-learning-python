import os
import shutil

path = './files/'
files = os.listdir(path)

for f in files:
    file_path = os.path.join(path, f)  # 文件的完整路径
    if os.path.isfile(file_path):  # 确保只对文件操作，排除目录
        folder_name = os.path.join(path, f.split('.')[-1])  # 目标文件夹路径
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)  # 创建文件夹
        shutil.move(file_path, folder_name)  # 移动文件