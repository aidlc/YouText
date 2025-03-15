import os
import time


def printENV():
    # 获取所有环境变量
    env_vars = os.environ
    # 打印指定的环境变量
    for key, value in env_vars.items():
        if key in ["OPENAI_API_KEY", "TAVILY_API_KEY", "ANTHROPIC_API_KEY", "GOOGLE_API_KEY"]:
            print(f"{key}: {value}")


def evalEndTime(start_time):
    end_time = time.time()  # 获取结束时间
    execution_time = "(程序运行时间：%.2f 秒)" % (
        end_time - start_time
    )  # 计算程序运行时间
    return execution_time


# --- 以下为调用函数的代码 ---

if __name__ == "__main__":
    start = time.time()
    
    printENV()  # 调用函数，打印环境变量

    # 程序主体可放在这里
    time.sleep(1)  # 模拟程序运行1秒钟
    
    # 打印程序运行时间
    print(evalEndTime(start))
