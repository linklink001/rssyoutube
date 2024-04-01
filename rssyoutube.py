import re
import requests

def get_channel_id(url):
    # 使用正则表达式匹配channel id
    pattern = r'youtube\.com\/channel\/([a-zA-Z0-9_-]+)'
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    else:
        # 检查是否为自定义URL
        custom_url_pattern = r'youtube\.com\/@([a-zA-Z0-9_-]+)'
        custom_match = re.search(custom_url_pattern, url)
        if custom_match:
            # 使用YouTube Data API的search.list方法
            api_url = 'https://www.googleapis.com/youtube/v3/search'
            params = {
                'part': 'snippet',
                'type': 'channel',
                'q': custom_match.group(1),
                'key': ''  # 需要替换成您的YouTube Data API密钥
            }
            response = requests.get(api_url, params=params)
            if response.status_code == 200:
                data = response.json()
                # 假设搜索结果中的第一个频道就是我们要找的频道
                if 'items' in data and len(data['items']) > 0:
                    return data['items'][0]['snippet']['channelId']
        return None

# 示例URL
url = input("请输入YouTube频道链接：")
channel_id = get_channel_id(url)
print(f'Channel ID: {channel_id}')
print(f"rss链接是：https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}")
input("按回车键退出...")
