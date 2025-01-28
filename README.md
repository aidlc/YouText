# youtube-transcript-tool
youtube-transcript-tool

执行脚本

```bash
$ python3 -V
$ python3 -m venv _yenv_
$ source _yenv_/bin/activate
$ cd  ~/youtube/YouText
$ python3 -m pip install --upgrade pip
# 安装库
$ pip install \
  langchain==0.2.14 \
  langchain-community==0.2.12 \
  langchain-aws==0.1.16 \
  langchain-openai==0.1.22 \
  langchainhub==0.1.21 \
  langgraph==0.2.34 \
  langchain-chroma==0.1.4 \
  wikipedia==1.4.0 \
  tavily-python==0.4.0 \
  python-dotenv==1.0.1

$ pip install pytube==15.0.0 \
  youtube-transcript-api==0.6.2

# 生成环境文件
cat << EOF > .env
OPENAI_API_KEY=123
TAVILY_API_KEY=456
ANTHROPIC_API_KEY=789
GOOGLE_API_KEY=XYZ
EOF

# 编辑程序
$ touch common.py
$ touch main.py
# 运行程序
$ python3 main.py
```
