# -*- coding: UTF-8 -*-  

from aip import AipSpeech
import cv2
import matplotlib.pyplot as plt
import base64

# 定义常量
APP_ID = '9851066'
API_KEY = 'LUGBatgyRGoerR9FZbV4SQYk'
SECRET_KEY = 'fB2MNz1c2UHLTximFlC4laXPg7CVfyjV'

# 初始化AipFace对象  
SpeechClient = AipSpeech(APP_ID, API_KEY, SECRET_KEY)



#语音文件
filePath = 'test.wav'

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
#imageType = "BASE64"

# 识别本地文件
result = SpeechClient.asr(get_file_content(filePath), 'wav', 16000, {
    'dev_pid': 1536,
})

print(result)
print result["result"][0]
