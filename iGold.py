import os
from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound

# 视频ID和频道名称
video_id = "5uc0mFC8Oo4"  # 请替换为实际的视频ID
channel_name = "iGold"  # 文件名友好的频道名称

# 创建保存字幕的文件夹
output_folder = "subtitles"
os.makedirs(output_folder, exist_ok=True)

try:
    # 列出可用字幕语言
    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
    print("Available transcript languages:")
    for transcript in transcript_list:
        print(f"Language: {transcript.language}, Language Code: {transcript.language_code}")

    # 获取英语字幕
    try:
        transcript = transcript_list.find_transcript(['en'])  # 查找英语字幕
        print("\nEnglish transcript found!")
    except NoTranscriptFound:
        print("\nEnglish transcript not available!")
        exit()

    # 保存原版字幕（英语）
    original_content = "\n".join(
        item['text'] for item in transcript.fetch() if item['text'] != "[Music]"
    )
    original_file_path = os.path.join(output_folder, f"original_transcript_{channel_name}.txt")
    with open(original_file_path, "w", encoding="utf-8") as f:
        f.write(original_content)
    print(f"\nOriginal transcript saved to {original_file_path}")

    # 翻译字幕为中文
    print("\nTranslating transcript to Simplified Chinese...")
    translated_transcript = transcript.translate('zh-Hans')  # 翻译为简体中文
    translated_content = "\n".join(
        item['text'] for item in translated_transcript.fetch() if item['text'] != "[Music]"
    )
    translated_file_path = os.path.join(output_folder, f"translated_transcript_{channel_name}.txt")
    with open(translated_file_path, "w", encoding="utf-8") as f:
        f.write(translated_content)
    print(f"Translated transcript saved to {translated_file_path}")

except NoTranscriptFound as e:
    print("Transcript retrieval failed:", e)
except Exception as e:
    print("An error occurred:", e)
