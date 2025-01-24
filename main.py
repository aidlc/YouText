from youtube_transcript_api import YouTubeTranscriptApi

# 视频ID
video_id = "iHrZKQQpuJQ"

# 列出可用字母
transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
# print(transcript_list)

# 获取字幕
transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
# print(transcript)
content = ""
for item in transcript:
    # print(item['text'])
    if item['text'] != "[Music]":
        content += item['text'] + " "

print(content)

# 翻译字幕
transcript = transcript_list.find_transcript(['en'])
translated_transcript = transcript.translate('zh-Hans')

content = ""
for item in translated_transcript.fetch():
    if item['text'] != "[音乐]":
        content += item['text'] + ""
print(content)