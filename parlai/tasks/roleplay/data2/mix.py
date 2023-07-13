import json

# 读取第一个文件
with open('rolplay.json', 'r') as f:
    data1 = json.load(f)

# 读取第二个文件
with open('converted_data.json', 'r') as f:
    data2 = json.load(f)

# 合并数据
merged_data = data1 + data2

# 删除所有'user'和'AI'字符
for conversation in merged_data:
    for dialogue in conversation['dialogue']:
        for role in dialogue:
            if isinstance(dialogue[role], str):
                dialogue[role] = dialogue[role].replace('user', '').replace('AI', '')

# 保存合并后的数据
with open('merged_data.json', 'w') as f:
    json.dump(merged_data, f)
