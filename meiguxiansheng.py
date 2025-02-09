import os
from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound

# 视频ID和频道名称
video_id = "OOxA6lHDVk8"  # 请替换为实际的视频ID
channel_name = "meiguxiansheng"  # 文件名友好的频道名称

# 创建保存字幕的文件夹
output_folder = "subtitles"
os.makedirs(output_folder, exist_ok=True)

try:
    # 列出可用字幕语言
    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
    print("支持的字幕语言:")
    for transcript in transcript_list:
        print(f"语言: {transcript.language}, 语言代码: {transcript.language_code}")

    # 获取汉语字幕
    try:
        transcript = transcript_list.find_transcript(['zh-Hans', 'zh-Hant', 'zh'])  # 查找简体中文或繁体中文字幕
        print("\n汉语字幕获取成功！")
    except NoTranscriptFound:
        print("\n汉语字幕不可用！")
        exit()

    # 保存原版字幕（汉语）
    original_content = "\n".join(
        item['text'] for item in transcript.fetch() if item['text'] != "[音乐]"
    )
    original_file_path = os.path.join(output_folder, f"original_transcript_{channel_name}.txt")
    with open(original_file_path, "w", encoding="utf-8") as f:
        f.write(original_content)
    print(f"\n原版字幕已保存为 {original_file_path}")

    # 翻译字幕为英文
    print("\n翻译为英文...")
    translated_transcript = transcript.translate('en')  # 翻译为英文
    translated_content = "\n".join(
        item['text'] for item in translated_transcript.fetch() if item['text'] != "[Music]"
    )
    translated_file_path = os.path.join(output_folder, f"translated_transcript_{channel_name}.txt")
    with open(translated_file_path, "w", encoding="utf-8") as f:
        f.write(translated_content)
    print(f"翻译后的字幕已保存为 {translated_file_path}")

except NoTranscriptFound as e:
    print("字幕获取失败：", e)
except Exception as e:
    print("发生错误：", e)
