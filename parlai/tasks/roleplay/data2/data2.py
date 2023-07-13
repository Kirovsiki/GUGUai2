import json

# 读取原始数据
with open('dialogs.txt', 'r') as f:
    lines = f.readlines()

# 转换数据
data = []
for i in range(0, len(lines), 2):
    dialogue = [
        {"role": "user", "content": lines[i].strip()}
    ]
    if i+1 < len(lines):  # 添加这个检查
        dialogue.append({"role": "ai", "content": lines[i+1].strip()})
    data.append({"dialogue": dialogue})

# 保存转换后的数据
with open('converted_data.json', 'w') as f:
    json.dump(data, f)
