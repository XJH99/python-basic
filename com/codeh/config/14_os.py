"""
文件和文件夹的操作：
    文件重命名：os.rename(⽬标⽂件名, 新⽂件名)
    删除文件：os.remove(⽬标⽂件名)
    创建文件夹：os.mkdir(⽂件夹名字)
    删除文件夹：os.rmdir(⽂件夹名字)
    获取当前目录：os.getcwd()
    改变默认目录：os.chdir(⽬录)
    获取目录列表：os.listdir(⽬录)
"""
# 批量文件名的修改
import os

flag = 2
dir_name = './'

file_list = os.listdir(dir_name)
print(file_list)

for name in file_list:
    if flag == 1:
        new_name = 'python_' + name
    elif flag == 2:
        num = len('python_')
        new_name = name[num:]

    print(new_name)

    os.rename(dir_name+name, dir_name+new_name)
