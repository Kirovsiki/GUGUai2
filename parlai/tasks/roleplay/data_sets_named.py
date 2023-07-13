import json
import random

def convert_dataset(input_file, output_file):
    names = ['Tim', 'Tom', 'KiKi', 'Alice', 'Bob''Alex', 'Lily', 'Max', 'Eva', 'Ben', 'Sophia', 'Daniel', 'Olivia', 'Lucas', 'Ava', 'Jacob', 'Emma', 'Leo', 'Mia', 'Oscar', 'Chloe', 'Henry', 'Grace', 'Ethan', 'Zoe']  # 添加更多的名字
    with open(input_file, 'r', encoding='utf-8') as fin, open(output_file, 'w', encoding='utf-8') as fout:
        episode = []
        episodes = []
        dialogue_count = 0  # 初始化对话计数器
        for line in fin:
            line = line.strip()
            if line == '':
                # end of episode
                if len(episode) > 0:
                    episodes.append({"dialogue": episode})
                    episode = []
                    dialogue_count += 1  # 增加对话计数器
            elif ': ' in line:
                role, text = line.split(': ', 1)
                if role.lower() == 'user':
                    role = random.choice(names)  # 随机选择一个名字
                elif role.lower() == 'ai':
                    role = 'GuGuAI'  # 将AI替换为GuGuAI
                episode.append({"role": role, "content": text})
        if len(episode) > 0:
            episodes.append({"dialogue": episode})
            dialogue_count += 1  # 增加对话计数器

        json.dump(episodes, fout, indent=2)

        # 打印对话总数
        print(f'Total dialogues: {dialogue_count}')

convert_dataset('test.txt', 'newtest.json')
