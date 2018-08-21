#!/usr/bin/python
#-*-coding:utf-8-*-       #指定编码格式，python默认unicode编码

import os

directory = "D:/downloads/user-pc/Desktop/test"

os.chdir(directory)  #切换到directory目录
cwd = os.getcwd()  #获取当前目录即dir目录下
print cwd

files = os.listdir(os.getcwd())  #列出目录下的文件
for file in files:
	os.remove(file)    #删除文件
	print(file + " deleted")