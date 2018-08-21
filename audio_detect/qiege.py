# -*- coding: UTF-8 -*-  


from pydub import AudioSegment 
import io

file_name = "my1.wav"

song = AudioSegment.from_wav("my1.wav")

step_time = 10

start_time = 0
end_time = 10

count = 0
i = 0

while i < 10000:
	
	temp1 = song[start_time * 1000 : end_time * 1000]
	#result_name = "pianduan" + str(count)+".wav"
	#temp1.export(result_name, format = "wav")
	start_time = start_time + step_time
	end_time = end_time + step_time
	count = count + 1
	i = i + step_time
	


print(song.duration_seconds)
print(len(song))
