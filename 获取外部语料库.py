import requests
import time
import os

# 示例 URL
url = 'https://www.gutenberg.org/files/1342/1342-0.txt'

# 确保目录存在
save_dir = os.path.dirname('C:\\Users\\20938\\Desktop\\自然语言处理大礼包\\自然语言处理大礼包\\项目架构示例\\data\\external_corpus.txt')
os.makedirs(save_dir, exist_ok=True)

# 重试参数
max_retries = 5
retry_delay = 2  # 秒

for attempt in range(max_retries):
    try:
        print(f"尝试下载 ({attempt + 1}/{max_retries})...")
        
        # 使用流式下载以更好地处理大文件
        with requests.get(url, stream=True, timeout=30) as response:
            response.raise_for_status()  # 检查请求是否成功
            
            # 保存语料库
            with open('C:\\Users\\20938\\Desktop\\自然语言处理大礼包\\自然语言处理大礼包\\项目架构示例\\data\\external_corpus.txt', 'w', encoding='utf-8') as file:
                # 分块写入，避免内存问题
                for chunk in response.iter_content(chunk_size=8192, decode_unicode=True):
                    file.write(chunk)
            
            print("外部语料库已成功保存到 external_corpus.txt")
            break  # 下载成功，跳出循环
            
    except requests.exceptions.RequestException as e:
        if attempt < max_retries - 1:
            print(f"下载失败 ({attempt + 1}/{max_retries}): {e}")
            print(f"将在 {retry_delay} 秒后重试...")
            time.sleep(retry_delay)
            retry_delay *= 2  # 指数退避，减少服务器负担
        else:
            print(f"下载失败，已达到最大重试次数: {e}")
            print("请检查网络连接或稍后再试。")
