# -*- coding: utf-8 -*-   
  
import os  

#函数作用：?取目?下文件名字，保存在file_name.txt中
#参数：文件目路径

def file_name(file_dir):   

    #文件名称写入路径
    f = open("file_name.txt","w")
    
    for root, dirs, files in os.walk(file_dir):
        pass
    
    print("?取中。。。。。")
    for file_name_get in files:
        f.write(file_name_get)
        f.write("\n")
    print("写入完成")
try:
    name = open("path.xml")
    file_path = name.readline()
    print(type(file_path))
except OSError as reason:
    print("error:%s" % reason)
file_name(file_path)
