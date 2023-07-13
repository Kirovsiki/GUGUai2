import json

# 读取你的数据集
with open('newtest.json', 'r') as f:
    data = json.load(f)

# 转换数据集
new_data = []
for episode in data:
    dialogue = []
    for turn in episode['dialogue']:
        # 去掉人名
        content = turn['content']
        for name in ['Tim', 'Tom', 'KiKi', 'Alice', 'Bob', 'Alex', 'Lily', 'Max', 'Eva', 'Ben', 'Sophia', 'Daniel', 'Olivia', 'Lucas', 'Ava', 'Jacob', 'Emma', 'Leo', 'Mia', 'Oscar', 'Chloe', 'Henry', 'Grace', 'Ethan', 'Zoe']:
            content = content.replace(name, '')
        dialogue.append({'role': turn['role'], 'content': content})
    new_data.append({'dialogue': dialogue})  # 添加对话到新的数据集

# 保存新的数据集
with open('test.json', 'w') as f:
    json.dump(new_data, f)
