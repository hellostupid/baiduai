#!/usr/bin/python
#-*-coding:utf-8-*-       #指定编码格式，python默认unicode编码

from aip import AipSpeech
import cv2
import matplotlib.pyplot as plt
import base64
from pydub import AudioSegment 
import io
import os

directory = "D:/downloads/user-pc/Desktop/test"

os.chdir(directory)  #切换到directory目录
cwd = os.getcwd()  #获取当前目录即dir目录下
print cwd

# 定义常量
APP_ID = '9851066'
API_KEY = 'LUGBatgyRGoerR9FZbV4SQYk'
SECRET_KEY = 'fB2MNz1c2UHLTximFlC4laXPg7CVfyjV'

# 初始化AipFace对象  
SpeechClient = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()






#语音文件
filePath = "my3.wav"

file_name = filePath

song = AudioSegment.from_wav(file_name)

step_time = 60

start_time = 0
end_time = 60

count = 0
i = 0

says = []

while i < 600000:
	
	temp1 = song[start_time * 1000 : end_time * 1000]
	result_name = "pianduan" + str(count)+".wav"
	temp1.export(result_name, format = "wav")
	#print(temp1.duration_seconds)
	start_time = start_time + step_time
	end_time = end_time + step_time
	
	i = i + step_time * 1000
	# 识别本地文件
	result = SpeechClient.asr(get_file_content(result_name), 'wav', 16000, {
    'dev_pid': 1536,})
	#print(result["err_no"])
	#print(result)
	print("宝宝还活着。。。宝宝还在运行。。。正在处理第%d文件>>>>>>>>>>fuck>>>>>>>>>>" % count)
	count = count + 1
	if result["err_no"] == 3301:
		os.remove(result_name)    #删除文件
		print(result_name + " deleted")
		continue
	else:
		#print(result)
		says.append(result["result"][0])

		#print(result["result"][0])
print("############################正文开始###########################################")
print()
for say in says:
	print say
print()
print("############################正文结束###########################################")

print("finish!!!!!!!!!!!fuck!!!!!!!!!!!!!")


#print(song.duration_seconds)
#print(len(song))





