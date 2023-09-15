import subprocess
from opencc import OpenCC


video_file_name   = 'video.mkv'
chs_srt_file_name = video_file_name[0:-5] + '.chs.srt'
cht_srt_file_name = video_file_name[0:-5] + '.cht.srt'
chs_srt_text      = ''
cht_srt_text      = ''
chs_srt_file      = ''
cht_srt_file      = ''

## Extract subtile from the video. 
cmd = "ffmpeg" + ' -i ' + video_file_name + ' -map 0:s:0 ' + chs_srt_file_name
subprocess.call(cmd, shell=True)

## Read from subtitle file. 
chs_srt_file  = open(chs_srt_file_name, 'r')
chs_srt_text  = chs_srt_file.read()
chs_srt_file.close()

## Convert to Traditional Chinese. 
converter     = OpenCC('s2t')
cht_srt_text  = converter.convert(chs_srt_text)
print(cht_srt_text)

## Save to subtitle file.
cht_srt_file  = open(cht_srt_file_name, 'w')
cht_srt_file.write(cht_srt_text)
cht_srt_file.close()




'''
ffmpeg -i chase.mkv -map 0:s:0 subs.srt

-i 表示输入文件
-map 表示视频中的那部分
0:s:0 第一个0表示第一个视频
0:s:0 s表示是字幕
0:s:0 第二个0表示第几个字幕文件
subs.srt表示输出文件名称
'''