import requests

# 这里假设豆包API的基础URL，实际要按官方给出的准确地址来写
BASE_API_URL = "https://api.doubao.com"  

# 构造请求数据，这里以简单的文本提问为例
data = {
    "question": "请介绍一下Python中的列表推导式",
    "parameters": {}  # 如果有其他参数需求，按API要求填写在此处
}

# 发送POST请求，通常认证等机制按API要求添加，这里暂简化处理
response = requests.post(BASE_API_URL + "/ask", json=data)

if response.status_code == 200:
    result = response.json()
    print(result["answer"])  # 假设返回的JSON数据中答案在"answer"字段里，按实际API规范为准
else:
    print(f"请求失败，状态码: {response.status_code}")
