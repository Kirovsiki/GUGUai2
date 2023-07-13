import json

# 读取你的数据集
with open('newroleplay.json', 'r') as f:
    data = json.load(f)

# 检查每个对话轮次
for episode in data:
    for turn in episode['dialogue']:
        assert isinstance(turn['content'], str), f"content is not a string: {turn}"
